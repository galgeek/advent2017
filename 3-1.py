import math

def taxi_distance(n):
    # find "taxi distance" of point on spiral to center 1
    # round square root to next odd number ~ rotation
    if n == 1:
        return 0

    c = math.ceil(math.sqrt(n))
    if c % 2 == 0:
        c += 1
    r = (c - 1) / 2

    lr = c ** 2
    cp = lr - n
    
    ep = cp % (2 * r)
    if ep <= r:
        nd = r + r - ep
    elif ep > r:
        nd = r + (ep - r)

    return int(nd)

n = int(input('n? '))
print('taxi distance of %s is %s' % (n, taxi_distance(n)))
