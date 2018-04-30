import sys

letters = 'abcdefghijklmnopqrstuvwxyz'

def gv(i, p):
    if len(i) == 1 and i in letters:
        if i not in registers[p]:
            registers[p][i] = 0
        return registers[p][i]
    else:
        return int(i)

lines = [line.split() for line in sys.stdin]

registers = { 0: {'p': 0}, 1: {'p':1} }

q = { 0: [], 1: [] }
sent = { 0: 0, 1: 0}

index = { 0: 0, 1: 0}

state = { 0: 'start', 1: 'start' }

#def prog(p, lines, registers, q, sent, index, state):
def prog(p):
    print('program ', p)
    if state[p] == 'done':
        print ('program ', p, ' done')
        return
    i = index[p]
    state[p] = 'running'
    while i < len(lines):
        l = lines[i]
        if l[0] == 'snd':
            q[p].append(gv(l[1], p))
            if p == 1:
                sent[1] += 1
        elif l[0] == 'rcv':
            if p == 0:
                op = 1
            else:
                op = 0
            if len(q[op]) > 0:
                registers[p][l[1]] = q[op].pop(0)
                state[p] = 'running'
            else:
                index[p] = i
                state[p] = 'waiting'
                break
        elif l[0] == 'set':
            registers[p][l[1]] = gv(l[2], p)
        elif l[0] == 'add':
            if l[1] in registers[p]:
                registers[p][l[1]] += gv(l[2], p)
            else:
                registers[p][l[1]] = gv(l[2],p)
        elif l[0] == 'mul':
            if l[1] in registers[p]:
                registers[p][l[1]] *= gv(l[2], p)
            else:
                registers[p][l[1]] = 0
        elif l[0] == 'mod':
            if l[1] in registers[p]:
                registers[p][l[1]] %= gv(l[2], p)
            else:
                registers[p][l[1]] = 0

        if l[0] == 'jgz' and gv(l[1], p) > 0:
            i += gv(l[2], p)
        else:
            i += 1
    if i >= len(lines):
        state[p] = 'done'

check_state = False
while not (state[0] == 'done' and state[1] == 'done'):
    prog(0)
    prog(1)
    if check_state and (state[0] != 'running' or state[1] != 'running'):
        break # done or deadlocked
    if check_state:
        check_state = False
    if (state[0] == 'done' and state[1] == 'waiting') or (state[0] == 'waiting' and state[1] == 'done'):
        check_state = True
    if state[0] == 'waiting' and state[1] == 'waiting':
        print('waiting')
        check_state = True

#part1 = result
part2 = sent[1]


#print(part1)
print(part2)
