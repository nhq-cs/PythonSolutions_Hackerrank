n = int(input())
num = list(map(int,input().split()))
index = max(num)
while max(num) ==index:
    num.remove(index)
print(max(num))
