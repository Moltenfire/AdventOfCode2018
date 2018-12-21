import collections
import itertools
import helper
import re

def addr(r, a, b, c):
    r[c] = r[a] + r[b]

def addi(r, a, b, c):
    r[c] = r[a] + b

def mulr(r, a, b, c):
    r[c] = r[a] * r[b]

def muli(r, a, b, c):
    r[c] = r[a] * b

def banr(r, a, b, c):
    r[c] = r[a] & r[b]

def bani(r, a, b, c):
    r[c] = r[a] & b

def borr(r, a, b, c):
    r[c] = r[a] | r[b]

def bori(r, a, b, c):
    r[c] = r[a] | b

def setr(r, a, b, c):
    r[c] = r[a]

def seti(r, a, b, c):
    r[c] = a

def gtir(r, a, b, c):
    r[c] = int(a > r[b])

def gtri(r, a, b, c):
    r[c] = int(r[a] > b)

def gtrr(r, a, b, c):
    r[c] = int(r[a] > r[b])

def eqir(r, a, b, c):
    r[c] = int(a == r[b])

def eqri(r, a, b, c):
    r[c] = int(r[a] == b)

def eqrr(r, a, b, c):
    r[c] = int(r[a] == r[b])

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
        func_name(reg, v[0], v[1], v[2])
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
