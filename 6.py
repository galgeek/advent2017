def do6(ins):
    cycles = 0
    banks = [int (i) for i in ins.split(' ')]
    #banks = [int (i) for i in ins.split('\t')]
    history = []
    while True:
        history.append(list(banks))
        m = 0
        for n in range(len(banks)):
            if banks[n] > m:
                m = banks[n]
                i = n
        blocksToShare = banks[i]
        banks[i] = 0
        for n in range(blocksToShare):
            i += 1
            if i == len(banks):
                i = 0
            banks[i] += 1
        cycles += 1
        print(banks)
        if banks in history:
            return cycles - history.index(banks)
            
in6 = input('in6? ')
print("{} cycles".format(do6(in6)))
