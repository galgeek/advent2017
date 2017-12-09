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
            checksum += (max(row) - min(row))

print(checksum)
