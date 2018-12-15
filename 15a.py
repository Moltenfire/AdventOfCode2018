import collections
import itertools
import helper
import re

HP = 200
ATTACK = 3

class Unit(object):
    def __init__(self, pos, race, attack):
        self.pos = pos
        self.race = race
        self.hp = HP
        self.attack = attack

    def alive(self):
        return self.hp > 0

    def __str__(self):
        return "{} {} {}".format(self.race, self.pos, self.hp)

def print_grid(grid, units, p=None):
    unit_pos = {u.pos : u.race for u in units}
    if p is not None:
        unit_pos[p] = unit_pos[p].lower()
    for y in range(grid.shape[1]):
        print(''.join(unit_pos[(x,y)] if (x,y) in unit_pos else c for x, c in enumerate(grid[:,y])))

    for u in units:
        print("{}{} HP:{}".format(u.race, u.pos, u.hp))

def setup(name, elf_attack=ATTACK):
    grid = helper.load_grid(name)
    units = []
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            c = grid[x,y]
            if c in "GE":
                attack = elf_attack if c == 'E' else ATTACK
                units.append(Unit((x,y),c, attack))
                grid[x,y] = '.'
    return grid, units

def get_adjacent(grid, pos):
    x = pos[0]
    y = pos[1]
    return [(i,j) for i,j in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)] if grid[i,j] == '.']

def get_all_targets(grid, units, unit):
    x = []
    for u in units:
        if u.race != unit.race and u.alive():
            x.extend(get_adjacent(grid, u.pos))
    return set(x)

def get_targets(grid, units, unit):
    a = set(get_adjacent(grid, unit.pos))
    t = [u for u in units if u.race != unit.race and u.alive() and u.pos in a]
    return t


def get_reachable(grid, units, pos):
    unit_pos = set([u.pos for u in units if u.alive()])
    positions = set()
    search = [pos]

    while len(search) > 0:
        new = set()
        for x,y in search:
            for i,j in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                if grid[i,j] == '.' and (i,j) not in unit_pos and (i,j) not in positions:
                    new.add((i,j))
            positions.add((x,y))
        search = list(new)

    return positions

def get_reachable_dist(grid, units, pos, ignore=None):
    unit_pos = set([u.pos for u in units if u.alive()])
    if ignore is not None:
        unit_pos.remove(ignore)
    positions = {}
    search = [pos]

    n = 0
    while len(search) > 0:
        new = set()
        for x,y in search:
            for i,j in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                if grid[i,j] == '.' and (i,j) not in unit_pos and (i,j) not in positions:
                    new.add((i,j))
            positions[(x,y)] = n
        search = list(new)
        n += 1

    return positions

def get_nearest_position(positions):
    min_dist = min(positions.values())
    nearest_positions = [k for k,v in positions.items() if v == min_dist]
    nearest_positions.sort(key=lambda pos : (pos[1], pos[0]))
    return nearest_positions[0]

def get_move(grid, units, unit):
    reachable = get_reachable(grid, units, unit.pos)
    all_targets = get_all_targets(grid, units, unit)
    possible_targets = reachable.intersection(all_targets)
    reachable_dist = get_reachable_dist(grid, units, unit.pos)
    positions = {p: reachable_dist[p] for p in possible_targets}
    if positions:
        nearest_position = get_nearest_position(positions)

        unit_pos = set([u.pos for u in units if u.alive()])
        possible_moves = [x for x in get_adjacent(grid, unit.pos) if x not in unit_pos]
        target_reachable_dist = {k : v for k,v in get_reachable_dist(grid, units, nearest_position, unit.pos).items() if k in possible_moves}
        possible_moves.sort(key=lambda pos : (target_reachable_dist[pos], pos[1], pos[0]))
        return possible_moves[0]

def round(n, grid, units, debug):
    units.sort(key=lambda unit : (unit.pos[1], unit.pos[0]))
    for i, unit in enumerate(units):
        # if debug:
            # print_grid(grid, units, unit.pos)
            # print(unit.pos)
        if not unit.alive():
            continue

        if len([u for u in units if u.alive() and u.race != unit.race]) == 0:
            return [u for u in units if u.alive()], True

        enemy_pos = set([u.pos for u in units if u.race != unit.race and u.alive()])
        next_to_enemy = len(enemy_pos.intersection(set(get_adjacent(grid, unit.pos)))) > 0

        # Move
        if not next_to_enemy:
            move = get_move(grid, units, unit)
            if move is not None:
                unit.pos = move

        # Attack
        targets = get_targets(grid, units, unit)
        if targets:
            targets.sort(key=lambda u : (u.hp, u.pos[1], u.pos[0]))
            target = targets[0]
            target.hp -= unit.attack

    return [u for u in units if u.alive()], False

def get_remaining_elfs(units):
    return len([u for u in units if u.race == 'E'])

def battle(grid, units, elf_death=False, debug=False):
    if debug:
        print()
        print_grid(grid, units)

    total_elfs = get_remaining_elfs(units)
    dead_elfs = 0

    n = 0
    while True:
        n += 1

        units, combat_ended = round(n, grid, units, debug)

        if elf_death:
            dead_elfs = total_elfs - get_remaining_elfs(units)
            if dead_elfs > 0:
                break

        if debug:
            print("Round", n)
            print_grid(grid, units)

        if combat_ended:
            n -= 1
            break

    total_hp = sum([u.hp for u in units])
    res = total_hp * n

    if elf_death:
        return res, n, total_hp, dead_elfs
    else:
        return res, n, total_hp

def part1(name, debug=False):
    grid, units = setup(name)
    return battle(grid, units, debug)

def part2(name, debug=False):
    for attack in itertools.count(4):
        grid, units = setup(name, attack)
        res, n, total_hp, dead_elfs = battle(grid, units, elf_death=True, debug=debug)
        if dead_elfs == 0:
            return res, n, total_hp, attack
        
        if debug:
            print(res, n, total_hp, attack, dead_elfs)

# print(part1('examples/15a.txt')) # 27730
# print(part1('examples/15b.txt')) # 36334
# print(part1('examples/15c.txt')) # 39514
# print(part1('examples/15d.txt')) # 27755
# print(part1('examples/15e.txt')) # 28944
# print(part1('examples/15f.txt')) # 18740
print(part1('input_15.txt'))

# print(part2('examples/15a.txt')) # 4988
# print(part2('examples/15c.txt')) # 31284
# print(part2('examples/15d.txt')) # 3478
# print(part2('examples/15e.txt')) # 6474
print(part2('input_15.txt'))
