from itertools import combinations as comb
n = int(input())
temp = list(map(str, input().split()))
index = int(input())
count = 0
compress = list(comb(temp,index))
for sub in compress:
    for i in range(index):
        if sub[i] =='a':
            count +=1
            break
answer = count / len(compress)
print('%.4f'%answer)
