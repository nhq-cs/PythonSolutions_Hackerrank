from itertools import combinations_with_replacement as cwp
from itertools import combinations

string, n = map(str, input().split())
string = list(string)
string.sort()
n = int(n)
answer = list(cwp(string,n))
arr = []
for sub in answer:
    temp = ''
    for key in sub:
        temp += key
    arr.append(temp)
for item in arr:
    print(item)
