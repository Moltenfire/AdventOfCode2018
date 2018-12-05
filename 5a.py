import helper

def collapse(l):
    while True:
        r = []
        i = 0
        while i < len(l) - 1:
            x = l[i]
            y = l[i+1]
            if x - 32 == y or x + 32 == y:
                r.append(i)
                i += 1
            i += 1

        if len(r) == 0:
            return len(l)
        for i in reversed(r):
            l.pop(i)
            l.pop(i)

s = helper.load_in_list('input_5.txt', str)[0]
# s = "dabAcCaCBAcCcaDA"
l = list(map(ord, s))

k = collapse(l)
print(k)

lengths = []
for i in range(65, 91):
    k = collapse([x for x in l if x != i and x - 32 != i])
    lengths.append(k)
print(min(lengths))
