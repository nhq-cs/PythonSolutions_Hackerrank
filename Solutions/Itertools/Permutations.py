from itertools import permutations as per
string, num = map(str, input().split())
num = int(num)
answer = list(per(string,num))
permu = []
for sub in answer:
    temp =''
    for key in sub:
        key = str(key)
        temp += key
    permu.append(temp)

permu.sort()
for item in permu:
    print(item)
