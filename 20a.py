import collections
import helper

def find_para(s):
    res = {}
    stack = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            res[stack.pop()] = i
    return res

def get_new_pos(c, p):
    if c == 'N':
        return (p[0], p[1]+1)
    if c == 'S':
        return (p[0], p[1]-1)
    if c == 'E':
        return (p[0]+1, p[1])
    if c == 'W':
        return (p[0]-1, p[1])

def gen_rooms(r, start, E):
    cur_pos = start
    para = find_para(r)

    i = 0
    while i < len(r):
        c = r[i]
        if c in "^$":
            i += 1
            continue
        if c in "NESW":
            new_pos = get_new_pos(c, cur_pos)
            E[cur_pos].append(new_pos)
            E[new_pos].append(cur_pos)
            cur_pos = new_pos
            i += 1
        if c == '(':
            last_para = para[i]
            inner_s = r[i+1:para[i]]
            gen_rooms(inner_s, cur_pos, E)
            i = last_para+1
        if c == '|':
            cur_pos = start
            i += 1

    return E

def get_distance(E, start):
    dists = {start : 0}
    q = set()
    q.add(start)
    
    while len(q) > 0:
        p = q.pop()
        for x in E[p]:
            if x not in dists:
                dists[x] = dists[p] + 1
                q.add(x)
    return dists
        

def start(r):
    E = collections.defaultdict(list)
    start = (0,0)
    gen_rooms(r, start, E)
    dists = get_distance(E, start)

    max_dist = max(dists.values())
    gt1000 = len([d for d in dists.values() if d >= 1000])

    return max_dist, gt1000

a = "^WNE$"
b = "^ENWWW(NEEE|SSE(EE|N))$"
c = "^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"
d = "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"
e = "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"
f = helper.load_in_list('input_20.txt', str)[0]

print(start(a))
print(start(b))
print(start(c))
print(start(d))
print(start(e))
print(start(f))
