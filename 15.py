def genAB(gena, genb, rounds):
    multA = 16807
    multB = 48271
    divider = 2147483647
    count = 0
    genAs = []
    genBs = []
    while len(genAs) <= rounds or len(genBs) <= rounds:
        gena = (gena * multA) % divider
        genb = (genb * multB) % divider
        if gena % 4 == 0:
            genAs.append(gena)
        if genb % 8 == 0:
            genBs.append(genb)
    for i in range(len(genBs)):
        if ((i < len(genAs)) and 
            (bin(genAs[i])[2:].zfill(32)[16:] == bin(genBs[i])[2:].zfill(32)[16:])):
            count += 1
    return count

gena = int(input('Gen A? '))
genb = int(input('Gen B? '))
rounds = int(input('rounds? '))
print("result   {}".format(genAB(gena, genb, rounds)))
