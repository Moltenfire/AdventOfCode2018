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

def main(part1=True):
    values = list(map(lambda x : (x.split()[0], list(map(int, x.split()[1:]))), helper.load_in_list('input_21.txt', str)))
    ip = 0
    ip_reg = values[0][1][0]
    program = values[1:]

    reg = [0,0,0,0,0,0]

    last = 0
    seen = set()
    while ip < len(program):

        if ip == 28:
            c = reg[2]
            if part1:
                print(c)
                break
            else:
                if c in seen:
                    print("Seen {} before. Last was {}".format(c, last))
                    break
                seen.add(c)
                last = c

        reg[ip_reg] = ip

        line = program[ip]
        func_name = func[line[0]]
        v = line[1]
        func_name(reg, v[0], v[1], v[2])
        ip = reg[ip_reg]
        ip += 1

if __name__ == '__main__':
    main()
    main(part1=False) # Warning this took 24mins
