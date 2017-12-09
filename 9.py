def do9(in9):
    score = 0
    groups = 0
    garbage = False
    cancelled = False
    g = 0
    with open(in9) as f:
        s = f.read()
    for c in s:
        if cancelled:
            cancelled = False
            continue
        if c == '!':
            cancelled = True
            continue
        if not garbage and c == '<':
            garbage = True
            continue
        if garbage:
            if c == '>':
                garbage = False
            else:
                g += 1
            continue
        if c == '{':
            groups += 1
        elif c == '}':
            score += groups
            groups -= 1
    return g

in9 = input('in9? ')
print("score {}".format(do9(in9)))
