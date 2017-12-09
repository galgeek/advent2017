def jumpins(fname):
    steps = 0
    i = 0
    with open(fname) as f:
        jumps = [int (i) for i in f.read().splitlines()]
    while i >= 0 and i < len(jumps):
        inc = jumps[i]
        if inc >= 3:
            jumps[i] -= 1
        else:
            jumps[i] += 1
        i += inc
        steps += 1
    return steps

jumpsfile = input('jumps file? ')
print("{} steps".format(jumpins(jumpsfile)))
