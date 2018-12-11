import numpy as np

def hundreds(x):
    if x < 100:
        return 0
    s = str(x)[-3]
    return int(s)

def get_power(x, y, serial):
    rankID = (x) + 10
    power = rankID * (y)
    power += serial
    power *= rankID
    power = hundreds(power)
    power -= 5
    return power

def gen_fuel_grid(serial, length):
    g = np.zeros((length, length))
    for x in range(length):
        for y in range(length):
            power = get_power(x+1, y+1, serial)
            g[x][y] = power

    return g

def largest(serial):
    length = 300
    g = gen_fuel_grid(serial, length)
    max_val = 0
    max_x = 0
    max_y = 0
    for x in range(length - 2):
        for y in range(length - 2):
            total = np.sum(g[x:x+3,y:y+3])
            if total > max_val:
                max_val = total
                max_x = x
                max_y = y
    return "{},{}".format(max_x+1, max_y+1), max_val

def largest_any_grid(serial):
    length = 300
    g = gen_fuel_grid(serial, length)
    max_val = 0
    max_x = 0
    max_y = 0
    max_grid = 0
    for s in range(1, 300):
        for x in range(length - s + 1):
            for y in range(length - s + 1):
                total = np.sum(g[x:x+s,y:y+s])
                if total > max_val:
                    max_val = total
                    max_x = x
                    max_y = y
                    max_grid = s
    return "{},{},{}".format(max_x+1, max_y+1, max_grid), max_val

# print(get_power(3,5, 8))
# print(get_power(122,79, 57))
# print(get_power(217,196, 39))
# print(get_power(101,153, 71))

# Part 1
# print(largest(18))
# print(largest(42))
print(largest(2568))

# Part 2
# print(largest_any_grid(18))
# print(largest_any_grid(42))
print(largest_any_grid(2568))
