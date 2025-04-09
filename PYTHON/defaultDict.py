from collections import defaultdict

d = defaultdict(list)
comand = input().split()
n = int(comand[0])
m = int(comand[1])
for i in range(n):
    value = input()    
    d['groupA'].append(value)

for i in range(m):
    value = input()    
    d['groupB'].append(value)

for i in d['groupB']:
    cont = 0
    result = []
    if i in d['groupA']:
        for _ in d['groupA']:
            cont += 1
            if _ == i:
                result.append(cont)
        print(' '.join(str(i) for i in result))
    else:
        print('-1')
    