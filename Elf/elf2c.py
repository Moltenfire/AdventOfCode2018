

def load_in_list(file, t=int):
    with open(file, 'r') as f:
        return list(map(lambda x : t(x.strip()), f.readlines()))

def write_start(f, ip):
    f.write('''static int r0, r1, r2, r3, r4, r5;

#include <stdio.h>

int main(int argc, char *argv[])
{
    r0 = r1 = r2 = r3 = r4 = r5 = 0;
''')
    f.write("    for(;;r{}++)\n".format(ip))
    f.write("    switch (r{}) {{\n".format(ip))

def write_end(f):
    f.write('''    default: printf("[%d,%d,%d,%d,%d,%d]\\n", r0, r1, r2, r3, r4, r5); return 0;
    }
}
''')

def addr(a, b, c):
    return "r{} = r{} + r{}".format(c, a, b)

def addi(a, b, c):
    return "r{} = r{} + {}".format(c, a, b)

def mulr(a, b, c):
    return "r{} = r{} * r{}".format(c, a, b)

def muli(a, b, c):
    return "r{} = r{} * {}".format(c, a, b)

def banr(a, b, c):
    return "r{} = r{} & r{}".format(c, a, b)

def bani(a, b, c):
    return "r{} = r{} & {}".format(c, a, b)

def borr(a, b, c):
    return "r{} = r{} | r{}".format(c, a, b)

def bori(a, b, c):
    return "r{} = r{} | {}".format(c, a, b)

def setr(a, b, c):
    return "r{} = r{}".format(c, a)

def seti(a, b, c):
    return "r{} = {}".format(c, a)

def gtir(a, b, c):
    return "r{} = {} > r{} ? 1 : 0".format(c, a, b)

def gtri(a, b, c):
    return "r{} = r{} > {} ? 1 : 0".format(c, a, b)

def gtrr(a, b, c):
    return "r{} = r{} > r{} ? 1 : 0".format(c, a, b)

def eqir(a, b, c):
    return "r{} = {} == r{} ? 1 : 0".format(c, a, b)

def eqri(a, b, c):
    return "r{} = r{} == {} ? 1 : 0".format(c, a, b)

def eqrr(a, b, c):
    return "r{} = r{} == r{} ? 1 : 0".format(c, a, b)

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

def write_inst(f, inst, args, i):
    s = func[inst](*args)
    f.write("    case {}: {}; break;\n".format(i, s))

def main():
    f = open("program.c", 'w')

    values = list(map(lambda x : (x.split()[0], list(map(int, x.split()[1:]))), load_in_list('../input_19.txt', str)))
    ip = values[0][1][0]
    program = values[1:]

    write_start(f, ip)

    for i, line in enumerate(program):
        write_inst(f, line[0], line[1], i)

    write_end(f)

if __name__ == '__main__':
    main()