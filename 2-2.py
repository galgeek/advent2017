fname = 'data.txt'
checksum = 0

with open(fname) as f:
    lines = f.read().splitlines()
    for line in lines:
        row = []
        for i in line.replace("\t", " ").split(" "):
            if i:
                row.append(int(i))
        if row != []:
            print(row)
            for i in range(len(row)):
                for j in range (len(row)):
                    if row[i] > row[j] and row[i] % row[j] == 0:
                            print(row[i], row[j])
                            checksum += (row[i] / row[j])
                            break
print(checksum)
