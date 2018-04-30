import knothash

# a small variation on VikeStep's solution, from which I learned much and admired...

key_string = 'hxtvlmkl'
#key_string = 'flqrgnkx'
unprocessed = []
regions = 0

for i in range(128):
    myHash = knothash.knothash(key_string + '-' + str(i))
    bin_hash = bin(int(myHash, 16))[2:].zfill(128)
    unprocessed += [(i, j) for j, d in enumerate(bin_hash) if d == '1']

print('1  ' + str(len(unprocessed)))

while unprocessed:
    queued = [unprocessed[0]]
    while queued:
        (x, y) = queued.pop()
        if (x, y) in unprocessed:
            unprocessed.remove((x, y))
            queued += [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    regions += 1

print('2  ' + str(regions))
