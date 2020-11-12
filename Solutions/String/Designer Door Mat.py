 n, m = map(int,input().split())
door = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(door + ['WELCOME'.center(m, '-')] + door[::-1])