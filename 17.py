import pdb

def solve(steps, maxIn):
    spinlock = [0]
    pos = 0
    for i in range(1, maxIn + 1):
        pos += steps
        while pos > (i - 1):
            pos -= i
        pos += 1
        if pos == 1:
            pos1 = i
        #spinlock = spinlock[:pos] + [i] + spinlock[pos:]
        # print(spinlock)
    #part1 = spinlock[pos + 1]
    part1 = None
    part2 = pos1
    print('part1: ', part1, '  part2: ', part2)

steps = int(input('steps? '))
maxIn = int(input('maxIn? '))
solve(steps,maxIn)
