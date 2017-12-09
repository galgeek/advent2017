def check_passphrases(fname):
    valid = 0
    total = 0
    with open(fname) as f:
        lines = f.read().splitlines()
        for line in lines:
            if check_anagram_passphrase(line):
                valid +=1
            total +=1
    print(valid, total)
    return valid, total

def check_passphrase(line):
    words = line.split(" ")
    s = set()
    for word in words:
        if word in s: return False
        s.add(word)
    return True

def check_anagram_passphrase(line):
    words = line.split(" ")
    s = set()
    for word in words:
        dorw = ''.join(sorted(word))
        if dorw in s: return False
        s.add(dorw)
    return True

#passphrase = input('passphrase? ')
#print("passphrase %s valid? %s!" % (passphrase, check_anagram_passphrase(passphrase)))

passphrasefile = input('file of passphrases? ')
valid, total = check_passphrases(passphrasefile)
print(" {} valid passphrases (of {} total)".format(valid, total))

