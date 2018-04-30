import sys
import numpy as np

iterations = 18

lines = [line.rstrip('\n') for line in sys.stdin]
rules = {}
for l in lines:
    rule = l.split(' => ')
    rules[rule[0]] = rule[1]


def make_grid(size):
    grid = np.zeros( (size,size), dtype=np.int16 )
    return grid


def fill_grid(grid, fill, x_offset=0, y_offset=0):
    for x, r in enumerate(fill):
        for y, c in enumerate(r):
            if c == '#':
                grid[x+x_offset,y+y_offset] = 1
    return grid

start = ['.#.','..#','###']
grid = make_grid(3)
grid = fill_grid(grid, start)


def enhance(square):
    square_orig = np.copy(square)
    fill = None
    i = 0
    while not fill and i < 10:
        key = ''
        for x, r in enumerate(square):
            if x != 0:
                key += '/'
            for y, c in enumerate(r):
                if c:
                    key += '#'
                else:
                    key += '.'
        if key in rules:
            fill = rules[key].split('/')
        else:
            if i == 0:
                square = np.fliplr(square_orig)
            elif i == 1:
                square = np.flipud(square_orig)
            elif i == 2:
                square = np.rot90(square_orig)
            elif i == 3:
                square = np.rot90(square_orig, 2)
            elif i == 4:
                square = np.rot90(square_orig, 3)
            elif i == 5:
                square = np.flipud(np.rot90(square_orig))
            elif i == 6:
                square = np.flipud(np.rot90(square_orig, 2))
            elif i == 7:
                square = np.flipud(np.rot90(square_orig, 3))
            elif i == 8:
                square = np.flipud(np.fliplr(square_orig))
            i += 1
    return fill


def update_grid(grid, size):
    new_grid = make_grid(int(grid.shape[0] / size) * (size + 1))
    x_off = 0
    for i in range(0, grid.shape[0]-1, size):
        y_off = 0
        for j in range(0, grid.shape[1]-1, size):
            fill = enhance(grid[i:i+size,j:j+size])
            #print(fill, x_off, y_off)
            new_grid = fill_grid(new_grid, fill, x_off, y_off)
            y_off += (size + 1)
        x_off += (size + 1)
    return new_grid
        
for i in range(iterations):
    if grid.shape[0] % 2 == 0:
        grid = update_grid(grid, 2)
    else: 
        grid = update_grid(grid, 3)

p1 = sum(sum(grid))
p2 = None

print('pixels on', p1)
