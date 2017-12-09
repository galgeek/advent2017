def do7(in7):
    programs = {}
    towers = {}
    with open(in7) as f:
        for line in f.read().splitlines():
            data = line.split(" ")
            programs[data[0]] = int(data[1][1:len(data[1])-1])
            if len(data) > 2:
                towers[data[0]] = ''.join(data[3:]).split(',')
    bottom = ''
    children = []
    for key in towers:
        for t in towers:
            if t in towers[key]:
                children.append(t)
    for key in towers:
        if key not in children:
            bottom = key
    for p in towers[bottom]:
        calc_weight(p, programs, towers)
    for p in towers[bottom]:
        find_unique(p, programs, towers)
    return bottom

def find_unique(p, programs, towers):
    weights = []
    if p in towers:
        for q in towers[p]:
            weights.append(programs[q])
        if max(weights) != min(weights):
            print(weights)
            maxq = []
            minq = []
            for q in towers[p]:
                print(q)
                if programs[q] == max(weights):
                    maxq.append(q)
                else:
                    minq.append(q)
            if len(maxq) == 1:
                if maxq[0] in towers:
                    find_unique(maxq[0], programs, towers)
                else:
                    print(maxq[0], programs[maxq[0]])
            elif len(minq) == 1:
                if minq[0] in towers:
                    find_unique(minq[0], programs, towers)
                else:
                    print(minq[0], programs[minq[0]])
    else:
        print(p, programs[p])


def calc_weight(p, programs, towers):
    if p in towers:
        for q in towers[p]:
            programs[p] += calc_weight(q, programs, towers)
    return programs[p]


in7 = input('in7? ')
print("{} bottom".format(do7(in7)))
