from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = list(product(a,b))
for item in answer:
    print(item, end=' ')
