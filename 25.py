from collections import defaultdict

tape = defaultdict(lambda: 0)

iterations = 12683008

p = 0
s = 'A'

for i in range(iterations):
    if s == 'A':
        if tape[p] == 0:
            tape[p] = 1
            p += 1
            s = 'B'
        else:
            tape[p] = 0
            p -= 1
            s = 'B'
    elif s == 'B':
        if tape[p] == 0:
            tape[p] = 1
            p -= 1
            s = 'C'
        else:
            tape[p] = 0
            p += 1
            s = 'E'
    elif s == 'C':
        if tape[p] == 0:
            tape[p] = 1
            p += 1
            s = 'E'
        else:
            tape[p] = 0
            p -= 1
            s = 'D'
    elif s == 'D':
        if tape[p] == 0:
            tape[p] = 1
            p -= 1
            s = 'A'
        else:
            tape[p] = 1
            p -= 1
            s = 'A'
    elif s == 'E':
        if tape[p] == 0:
            tape[p] = 0
            p += 1
            s = 'A'
        else:
            tape[p] = 0
            p += 1
            s = 'F'
    elif s == 'F':
        if tape[p] == 0:
            tape[p] = 1
            p += 1
            s = 'E'
        else:
            tape[p] = 1
            p -= 1
            s = 'A'

diagnostic = sum(tape.values())

print(diagnostic)