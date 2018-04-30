def do12(inp):
    programs = {}
    with open(inp) as f:
        for line in f.read().splitlines():
            els = line.split(' ',2)
            programs[int(els[0])] = [int(i) for i in els[2].split(',')]
    group = programs
    for i in range(len(group)):
        while True:
            ps = len(group[i])
            for j in group[i]:
                for k in programs[j]:
                    if k not in group[i]:
                        group[i].append(k)
            if ps == len(group[i]):
                group[i].sort()
                break

    unique_g = [group[0]]
    for i in range(1, len(group)):
        if group[i] not in unique_g:
            unique_g.append(group[i])
    return len(unique_g)


inp = input('input? ')
print("result   {}".format(do12(inp)))
