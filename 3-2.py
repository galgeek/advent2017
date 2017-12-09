def move_right(x,y):
    return x+1, y

def move_down(x,y):
    return x,y-1

def move_left(x,y):
    return x-1,y

def move_up(x,y):
    return x,y+1

moves = [move_right, move_up, move_left, move_down]

def spiral_value_ceil(end):
    # find first spiral value > end
    from itertools import cycle
    _moves = cycle(moves)
    pos = 0,0
    points = {}
    times_to_move = 1

    points[pos] = 1

    while True:
        for _ in range(2):
            move = next(_moves)
            for _ in range(times_to_move):
                if points[pos] > end:
                    return points[pos]
                pos = move(*pos)
                points[pos] = populate_spiral(pos, points)

        times_to_move += 1

def populate_spiral(pos, points):
    n = 0
    x, y = pos
    xPlus = x + 1
    xLess = x - 1
    yPlus = y + 1
    yLess = y - 1

    if (xLess,y) in points:
        n += points[(xLess,y)]
    if (xLess,yLess) in points:
        n += points[(xLess,yLess)]
    if (x,yLess) in points:
        n += points[(x,yLess)]
    if (xPlus,yLess) in points:
        n += points[(xPlus,yLess)]
    if (xPlus,y) in points:
        n += points[(xPlus,y)]
    if (xPlus,yPlus) in points:
        n += points[(xPlus,yPlus)]
    if (x,yPlus) in points:
        n += points[(x,yPlus)]
    if (xLess,yPlus) in points:
        n += points[(xLess,yPlus)]
    return n

n = int(input('n? '))
print('spiral value just greater than %s is %s' % (n, spiral_value_ceil(n)))
