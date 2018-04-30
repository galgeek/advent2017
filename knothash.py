def knothash(inp):
    pos = 0
    skip = 0

    hash10 = []
    #len_hash = 5 # test list
    len_hash = 256
    for i in range(len_hash):
        hash10.append(i)

    # lengths = [int(i) for i in inp.split(',')] # round 1
    lengths = []
    for c in inp:
        lengths.append(int(ord(c)))
    lengths += [17, 31, 73, 47, 23]
    #print(lengths)

    for i in range(64):
        for l in lengths:
            if l > 1: 
                hash10 = hash_update(hash10, pos, l)
            pos += (l + skip)
            while pos > len(hash10):
                pos -= len(hash10)
            skip += 1

    densehash = []
    for i in range(16):
        densehash.append(hash10[16*i+0] ^ hash10[16*i+1] ^ hash10[16*i+2] ^ hash10[16*i+3] ^
                         hash10[16*i+4] ^ hash10[16*i+5] ^ hash10[16*i+6] ^ hash10[16*i+7] ^
                         hash10[16*i+8] ^ hash10[16*i+9] ^ hash10[16*i+10] ^ hash10[16*i+11] ^
                         hash10[16*i+12] ^ hash10[16*i+13] ^ hash10[16*i+14] ^ hash10[16*i+15])
    knothash = ''
    for i in densehash:
        knothash += hex(i)[2:].zfill(2)

    # return hash10[0] * hash10[1] # round 1
    return knothash


def hash_update(a, start, length):
    arc = (a * 2)[start:start+length]
    revarc = arc[::-1]
    if start + length < len(a):
        a1 = a[:start]
        a2 = revarc
        a3 = a[start+length:]
    else:
        a3 = revarc[:len(a)-start]
        a1 = revarc[len(a3):]
        a2 = a[len(a1):len(a)-len(a3)]
    return a1 + a2 + a3


#inp = input('input? ')
#print("knothash   {}".format(knothash(inp)))
