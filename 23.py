import sys
from collections import defaultdict

registers = defaultdict(lambda: 0)
registers['a'] = 1

lines = [line.rstrip('\n').split() for line in sys.stdin]

letters = 'abcdefgh'
#letters = 'abcdefghijklmnopqrstuvwxyz'

def gv(i):
    if len(i) == 1 and i in letters:
        return registers[i]
    else:
        return int(i)

i = 0
mult = 0
while i < len(lines):
    l = lines[i]
    if l[0] == 'set':
        registers[l[1]] = gv(l[2])
    elif l[0] == 'sub':
       registers[l[1]] -= gv(l[2])
    elif l[0] == 'mul':
        mult += 1
        registers[l[1]] *= gv(l[2])

    if l[0] == 'jnz' and gv(l[1]) != 0:
        i += gv(l[2])
    else:
        i += 1

part1 = registers['h']
part2 = None


print(part1)
print(part2)
