import sys
from collections import defaultdict

lines = [line.rstrip('\n').split('/') for line in sys.stdin]
parts = defaultdict(lambda: [])
for line in lines:
    p = (int(line[0]),int(line[1]))
    parts[p[0]].append(p)
    if p not in parts[p[1]]:
        parts[p[1]].append(p)

bridges = []
strengths = []
lengths = []

def add_part(b, port, strength, length):
    matches = parts[port]
    if len(matches) > 1: # we'll match current part at least
        for m in matches:
            if m not in b:
                bToo = list(b)
                bToo.append(m)
                newlength = length + 1
                lengths.append(newlength)
                bridges.append(bToo)
                c1, c2 = m
                newstrength = strength + c1 + c2
                strengths.append(newstrength)
                if port == c2:
                    newport = c1
                else:
                    newport = c2
                add_part(bToo, newport, newstrength, newlength)


for p in parts[0]:
    bridges.append([p]) # one-part bridges
    c1, c2 = p
    if c1:
        port = c1
    else:
        port = c2
    strength = c1 + c2
    lengths.append(1)
    strengths.append(strength)
    add_part([p], port, strength, 1)

print(max(strengths))
maxlength = max(lengths)
maxlengths = [index for index, value in enumerate(lengths) if value == maxlength]
maxls = strengths[maxlengths[0]]
if len(maxlengths) > 1:
    for i in range(1, len(maxlengths)):
        if strengths[maxlengths[i]] > maxls:
            maxls = strengths[maxlengths[i]]
print(maxls)
