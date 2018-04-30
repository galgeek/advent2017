import sys
import re

iterations = 1000
md = []

patt = re.compile('p=<(-?[\d]+),(-?[\d]+),(-?[\d]+)>, v=<(-?[\d]+),(-?[\d]+),(-?[\d]+)>, a=<(-?[\d]+),(-?[\d]+),(-?[\d]+)>.*')
ps = []
for line in sys.stdin:
    m = patt.match(line)
    ps.append([[int(m[1]),int(m[2]),int(m[3])],[int(m[4]),int(m[5]),int(m[6])],[int(m[7]),int(m[8]),int(m[9])]])


for i in range(iterations):
    for j in range(len(ps)):
        ps[j][1][0] += ps[j][2][0]
        ps[j][1][1] += ps[j][2][1]
        ps[j][1][2] += ps[j][2][2]
        ps[j][0][0] += ps[j][1][0]
        ps[j][0][1] += ps[j][1][1]
        ps[j][0][2] += ps[j][1][2]

    colliding = set()
    k, l = 0, 1
    while k <len(ps):
        while l < len(ps):
            if ps[l][0] == ps[k][0]:
                colliding.add(k)
                colliding.add(l)
            l += 1
        k += 1
        l = k + 1
    deleteMe = sorted(colliding, reverse=True)
    for d in range(len(deleteMe)):
        del ps[deleteMe[d]]
        
    
'''
part1
minP = None
minPS = None
for j in range(len(ps)):
    pP = abs(ps[j][0][0]) + abs(ps[j][0][1]) + abs(ps[j][0][2])
    if not minP:
        minP = pP
        minPS = j
    else:
        if pP < minP:
            minP = pP
            minPS = j


print('particle ',minPS, ' distance ',minP)
'''

print('particles remaining ', len(ps))
