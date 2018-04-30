import sys
from collections import defaultdict

iterations = 10000000
grid = defaultdict(lambda: ".")

lines = [list(line.rstrip('\n')) for line in sys.stdin]

for y, l in enumerate(lines):
    for x, c in enumerate(l):
        if c == '#':
            grid[(x,y)] = c

infections = 0 # new infections
center = round(len(lines)/2)
p = (center,center)
d = 'u'

for i in range(iterations):
    current_node = grid[p]
    if current_node == '.':
        grid[p] = 'W'
        if d == 'u':
            p = (p[0]-1,p[1])
            d = 'l'
        elif d == 'd':
            p = (p[0]+1,p[1])
            d = 'r'
        elif d == 'r': 
            p = (p[0],p[1]-1)
            d = 'u'
        elif d == 'l': 
            p = (p[0],p[1]+1)
            d = 'd'
    elif current_node == 'W':
        grid[p] = '#'
        infections += 1
        if d == 'u':
            p = (p[0],p[1]-1)
        elif d == 'd':
            p = (p[0],p[1]+1)
        elif d == 'r': 
            p = (p[0]+1,p[1])
        elif d == 'l': 
            p = (p[0]-1,p[1])
    elif current_node == '#':
        grid[p] = 'F'
        if d == 'u':
            p = (p[0]+1,p[1])
            d = 'r'
        elif d == 'd':
            p = (p[0]-1,p[1])
            d = 'l'
        elif d == 'r': 
            p = (p[0],p[1]+1)
            d = 'd'
        elif d == 'l': 
            p = (p[0],p[1]-1)
            d = 'u'
    elif current_node == 'F':
        grid[p] = '.'
        if d == 'u':
            p = (p[0],p[1]+1)
            d = 'd'
        elif d == 'd':
            p = (p[0],p[1]-1)
            d = 'u'
        elif d == 'r': 
            p = (p[0]-1,p[1])
            d = 'l'
        elif d == 'l': 
            p = (p[0]+1,p[1])
            d = 'r'

p1 = infections

print(p1)
#print(p2)
