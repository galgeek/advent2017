import sys

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

lines = [list(line) for line in sys.stdin]

# find start
for i in range(len(lines[0])):
    if lines[0][i] == '|':
        d = 'd'
        x = i
        print('found start!')

y = 1

path = ''

steps = 1

while d:
    if d == 'd':
        if lines[y][x] == '|':
            y += 1
            steps += 1
        elif lines[y][x] == '-':
            y += 1
            steps += 1
        elif lines[y][x] in letters:
            path += lines[y][x]
            print(path)
            y += 1
            steps += 1
        elif lines[y][x] == '+':
            d = 'tlr'
            steps += 1
        elif lines[y][x] == ' ':
            d = None
    elif d == 'u':
        if lines[y][x] == '|':
            y -= 1
            steps += 1
        elif lines[y][x] == '-':
            y -= 1
            steps += 1
        elif lines[y][x] in letters:
            path += lines[y][x]
            print(path)
            y -= 1
            steps += 1
        elif lines[y][x] == '+':
            d = 'tlr'
            steps += 1
        elif lines[y][x] == ' ':
            d = None
    elif d == 'tlr':
        if lines[y][x-1] != ' ':
            d = 'l'
            x -=1
        elif lines[y][x+1] != ' ':
            d = 'r'
            x += 1
    elif d == 'l':
        if lines[y][x] == '-':
            x -= 1
            steps += 1
        elif lines[y][x] == '|':
            x -= 1
            steps += 1
        elif lines[y][x] in letters:
            path += lines[y][x]
            print(path)
            x -= 1
            steps += 1
        elif lines[y][x] == '+':
            d = 'tdu'
            steps += 1
        elif lines[y][x] == ' ':
            d = None
    elif d == 'r':
        if lines[y][x] == '-':
            x += 1
            steps += 1
        elif lines[y][x] == '|':
            x += 1
            steps += 1
        elif lines[y][x] in letters:
            path += lines[y][x]
            print(path)
            x += 1
            steps += 1
        elif lines[y][x] == '+':
            d = 'tdu'
            steps += 1
        elif lines[y][x] == ' ':
            d = None
    elif d == 'tdu':
        if lines[y-1][x] != ' ':
            d = 'u'
            y -=1
        elif lines[y+1][x] != ' ':
            d = 'd'
            y += 1
    continue



    

part1 = path
part2 = steps


print(part1)
print(part2)
