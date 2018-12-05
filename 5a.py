import helper

def collapse(l):
    stack = []
    for y in l:
        if not stack:
            stack.append(y)
        else:
            x = stack[-1]
            if x - 32 == y or x + 32 == y:
                stack.pop()
            else:
                stack.append(y)
    return len(stack)

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
