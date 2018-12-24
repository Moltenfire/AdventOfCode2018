import collections
import itertools
import helper
import re
import copy

class Group():
    def __init__(self, immune, i, total, hp, attack, initiative, attack_type, weak, resistance):
        self.immune = immune
        self.id = i
        self.total = total
        self.hp = hp
        self.attack = attack
        self.initiative = initiative
        self.attack_type = attack_type
        self.weak = weak
        self.resistance = resistance

    def damage(self):
        return self.total * self.attack

    def __repr__(self):
        s = "Immune" if self.immune else "Infection"
        return "{} group {}, {} units".format(s, self.id, self.total)

def create_unit(line, immune, i):
    total, hp, attack, initiative = list(map(int, re.findall("-?\d+", line)))
    weak, res = set(), set()
    if "(" in line:
        x = line.split("(")[1]
        y = x.split(")")[0]
        for s in y.split("; "):
            if "weak" in s:
                weak = set(s[len("weak to "):].split(", "))
            if "immune" in s:
                res = set(s[len("immune to "):].split(", "))
    attack_type = line.split()[-5]
    return Group(immune, i, total, hp, attack, initiative, attack_type, weak, res)
                
def setup():
    groups = []
    values = helper.load_in_list("input_24.txt", str)
    immune = True
    i = 1
    for line in values:
        if "Infection" in line:
            immune = False
            i = 1
            continue
        if line == "" or "Immune System" in line:
            continue
        g = create_unit(line, immune, i)
        groups.append(g)
        i += 1
    return groups

def potential_dmg(g1, g2):
    at = g1.attack_type
    if g1.attack_type in g2.resistance:
        return 0
    dmg = g1.damage()
    if g1.attack_type in g2.weak:
        dmg *= 2
    return dmg

def battle(g, bonus=0):

    groups = copy.deepcopy(g)

    for g in groups:
        if g.immune:
            g.attack += bonus

    while True:

        # print("\nImmune System:")
        im = [g for g in groups if g.immune]
        # for x in im:
        #     print(x)
        # print("\nInfection:")
        iff = [g for g in groups if not g.immune]
        # for x in iff:
        #     print(x)

        if len(im) == 0 or len(iff) == 0:
            total = [g.total for g in groups]
            # print(total)
            return sum(total), len(im) > 0
        
        targets = {}
        groups.sort(key=lambda x : (x.damage(), x.initiative), reverse=True)
        for g in groups:
            dmg = {}
            for e in [e for e in groups if g.immune != e.immune and e not in targets.values()]:
                d = potential_dmg(g, e)
                if d > 0:
                    dmg[e] = d
            enimies = list(dmg.keys())
            if len(enimies) > 0:
                enimies.sort(key=lambda x : (dmg[x], x.damage(), x.initiative), reverse=True)
                e =  enimies[0]
                targets[g] = e

        tt = list(targets.keys())
        tt.sort(key=lambda x : x.initiative, reverse=True)
        for t in tt:
            d = targets[t]
            dmg = potential_dmg(t, d)
            kills = int( min(dmg, d.hp * d.total) / d.hp)
            d.total -= kills
            # print("{} attacks {} dmg {} kills {}".format(t, d, dmg, kills))

        groups = [g for g in groups if g.total > 0]
    

def main():
    groups = setup()

    total, won = battle(groups)
    print(total)

    for i in itertools.count(39):
        total, won = battle(groups, i)
        if won:
            print(i, total)
            break



if __name__ == '__main__':
    main()
