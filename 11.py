def do11(inp):
    with open(inp) as f:
        s = f.read().rstrip('\n')
    center = (0, 0, 0) # x, y, z
    md = 0
    p = center
    steps = s.split(',')
    print(steps)
    for s in steps:
        if s == 'n':
            p = (p[0], p[1]+1, p[2]-1)
        elif s == 'ne':
            p = (p[0]+1, p[1], p[2]-1)
        elif s == 'se':
            p = (p[0]+1, p[1]-1, p[2])
        elif s == 's':
            p = (p[0], p[1]-1, p[2]+1)
        elif s == 'sw':
            p = (p[0]-1, p[1], p[2]+1)
        elif s == 'nw':
            p = (p[0]-1, p[1]+1, p[2])
        d = cube_distance(center, p)
        if d > md:
            md = d
    return md # return max distance from center
    # return d # return last distance from center

def cube_distance(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))

inp = input('input? ')
print("result   {}".format(do11(inp)))
