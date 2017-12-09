registers = {}

def do8(in8):
    localmax = 0
    with open(in8) as f:
        for line in f.read().splitlines():
            elements = line.split(' ')
            # set registers, if they don't exist
            if elements[0] not in registers:
                registers[elements[0]] = 0
            if elements[4] not in registers:
                registers[elements[4]] = 0
            # eval conditional
            if elements[5] == '==':
                conditional = registers[elements[4]] == int(elements[6])
            elif elements[5] == '!=':
                conditional = registers[elements[4]] != int(elements[6])
            elif elements[5] == '>':
                conditional = registers[elements[4]] > int(elements[6])
            elif elements[5] == '>=':
                conditional = registers[elements[4]] >= int(elements[6])
            elif elements[5] == '<':
                conditional = registers[elements[4]] < int(elements[6])
            elif elements[5] == '<=':
                conditional = registers[elements[4]] <= int(elements[6])
            # update reg
            if conditional:
                if elements[1] == 'inc':
                    registers[elements[0]] += int(elements[2])
                elif elements[1] == 'dec':
                    registers[elements[0]] -= int(elements[2])
            if registers[max(registers, key=registers.get)] > localmax:
                localmax = registers[max(registers, key=registers.get)]
    return localmax
            
in8 = input('in8? ')
print("{} max".format(do8(in8)))
