data = []

rom_symbols={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

with open('../p089_roman.txt', 'r') as openfileobject:
    for line in openfileobject:
        data.append(line)

for i in range(len(data)-1):
    data[i]=data[i][:-1]

def T(d):
    d=d.replace('VIIII', 'IX')
    d=d.replace('LXXXX', 'XC')
    d=d.replace('IIII', 'IV')
    d=d.replace('XXXX', 'XL')
    d=d.replace('DCCCC', 'CM')
    d=d.replace('CCCC', 'CD')
    return d

minim = [T(d) for d in data]

out = sum(len(data[i])-len(minim[i]) for i in range(len(data)))
print(out)