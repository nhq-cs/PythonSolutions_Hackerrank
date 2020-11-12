from itertools import combinations as com
string, n = map(str, input().split())
string = list(string)
string.sort()
n = int(n)
combination = []
for i in range(1, n+1):
    answer = list(com(string, i))
    for sub in answer:
        temp = ''
        for key in sub:
            temp += key
        combination.append(temp)
for item in combination:
    print(item)
