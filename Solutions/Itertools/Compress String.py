from itertools import groupby
string = input()
print(*[(len(list(c)), int(num)) for num,c in groupby(string)])
