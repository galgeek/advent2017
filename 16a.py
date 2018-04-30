import sys

#programs=['a','b','c','d','e']
programs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
moves = []

'''
programs = {}

for i in range(len(letters)):
    programs[letters[i]] = i
print(programs)
'''

for line in sys.stdin:
    moves += line.split(',')

for m in moves:
    move = m[0]
    if move == 's':
        n = int(m[1])
        programs = programs[-n:] + programs[:len(programs)-n]
    elif move == 'x' or move == 'p':
        if move == 'x':
            a,b = map(int, m[1:].split('/'))
        else:
            aPos,bPos = m[1:].split('/')
            a = programs.index(aPos[0])
            b = programs.index(bPos[0])

        if a > b:
            smaller = b
            b = a
            a = smaller
        if programs[a] == programs[0]:
            start = []
        else:
            start = programs[:a]
        if programs[b] == programs[-1]:
            end = []
        else:
            end = programs[b+1:]
        programs = start + [programs[b]] + programs[a+1:b] + [programs[a]] + end

    #print(m, programs)

part1 = ''.join(programs)
part2 = None 

print(part1)
print(part2)
