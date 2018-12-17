import collections
import itertools
import helper
import re

def setup():
    values = helper.load_in_list('input_16.txt', str)
    before = []
    reg = []
    after = []
    for s in values:
        x = list(map(int, re.findall("-?\d+", s)))
        if len(x) > 0:
            if "Before" in s:
                before.append(x)
            elif "After" in s:
                after.append(x)
            else:
                reg.append(x)
    return zip(before, reg, after)

def addr(registers, a, b, c):
    res = registers[::]
    res[c] = res[a] + res[b]
    return res

def addi(registers, a, b, c):
    res = registers[::]
    res[c] = res[a] + b
    return res

def mulr(registers, a, b, c):
    res = registers[::]
    res[c] = res[a] * res[b]
    return res

def muli(registers, a, b, c):
    res = registers[::]
    res[c] = res[a] * b
    return res

def banr(registers, a, b, c):
    res = registers[::]
    res[c] = res[a] & res[b]
    return res

def bani(registers, a, b, c):
    res = registers[::]
    res[c] = res[a] & b
    return res

def borr(registers, a, b, c):
    res = registers[::]
    res[c] = res[a] | res[b]
    return res

def bori(registers, a, b, c):
    res = registers[::]
    res[c] = res[a] | b
    return res

def setr(registers, a, b, c):
    res = registers[::]
    res[c] = res[a]
    return res

def seti(registers, a, b, c):
    res = registers[::]
    res[c] = a
    return res

def gtir(registers, a, b, c):
    res = registers[::]
    res[c] = 1 if a > res[b] else 0
    return res

def gtri(registers, a, b, c):
    res = registers[::]
    res[c] = 1 if res[a] > b else 0
    return res

def gtrr(registers, a, b, c):
    res = registers[::]
    res[c] = 1 if res[a] > res[b] else 0
    return res

def eqir(registers, a, b, c):
    res = registers[::]
    res[c] = 1 if a == res[b] else 0
    return res

def eqri(registers, a, b, c):
    res = registers[::]
    res[c] = 1 if res[a] == b else 0
    return res

def eqrr(registers, a, b, c):
    res = registers[::]
    res[c] = 1 if res[a] == res[b] else 0
    return res

test = ([3, 2, 1, 1], [9, 2, 1, 2], [3, 2, 2, 1])
instructions = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

def check_instrunction(i, r):
    res = instructions[i](r[0], r[1][1], r[1][2], r[1][3])
    return res == r[2]

def behaves_like(r):
    return [inst for inst in range(len(instructions)) if check_instrunction(inst, r)]

def behaves_like3ormore(values):
    return len([x for x in values if len(behaves_like(x)) > 2])

def part1():
    values = setup()
    res = behaves_like3ormore(values)
    print(res)

def get_op2inst():
    values = setup()
    results = collections.defaultdict(list)
    all_ops = set()
    for v in values:
        res = behaves_like(v)
        if len(res) > 0:
            opcode = v[1][0]
            results[opcode].append(set(res))
            all_ops.add(opcode)
    
    inst2op = collections.defaultdict(set)
    for k, v in results.items():
        n = v[0]
        for i in range(1, len(v)):
            n = n.intersection(v[i])
        for x in n:
            inst2op[x].add(k)

    op2inst = {}
    while True:
        for inst, ops in inst2op.items():
            if len(ops) == 1:
                op2inst[list(ops)[0]] = inst
        for op in op2inst:
            for inst, ops in inst2op.items():
                if op in ops:
                    ops.remove(op)
        
        if len(op2inst) == len(all_ops):
            break

    return op2inst

def part2():
    op2inst = get_op2inst()

    program = list(map(lambda x : list(map(int, re.findall("-?\d+", x))), helper.load_in_list('input_16_2.txt', str)))
    
    reg = [0,0,0,0]
    for line in program:
        inst = op2inst[line[0]]
        reg = instructions[inst](reg, line[1], line[2], line[3])

    print(reg)

part1()
part2()
