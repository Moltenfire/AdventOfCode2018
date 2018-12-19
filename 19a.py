import collections
import itertools
import helper
import re

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

func = {
    "addr" : addr,
    "addi" : addi,
    "mulr" : mulr,
    "muli" : muli,
    "banr" : banr,
    "bani" : bani,
    "borr" : borr,
    "bori" : bori,
    "setr" : setr,
    "seti" : seti,
    "gtir" : gtir,
    "gtri" : gtri,
    "gtrr" : gtrr,
    "eqir" : eqir,
    "eqri" : eqri,
    "eqrr" : eqrr
}

def main(n=0):
    values = list(map(lambda x : (x.split()[0], list(map(int, x.split()[1:]))), helper.load_in_list('input_19.txt', str)))
    ip = 0
    ip_reg = values[0][1][0]
    program = values[1:]

    reg = [n,0,0,0,0,0]
    t = 0
    while ip < len(program):
        reg[ip_reg] = ip

        line = program[ip]
        func_name = func[line[0]]
        v = line[1]
        reg = func_name(reg, v[0], v[1], v[2])
        ip = reg[ip_reg]
        ip += 1
    
        # print(reg, line[0], v)
        # t += 1
        # if t > 100:
        #     break

    print(reg)

if __name__ == '__main__':
    main()
    # main(1)
