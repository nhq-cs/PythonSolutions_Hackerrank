def newstring(string):
    temp = ''
    for char in string:
        if char not in temp:
            temp += char
    return temp
def merge_the_tools(string, k):
    mysplit = []
    division = len(string)//k
    if k==1:
        for item in string:
            print(item)
    else:
        while len(string) >=division:
            temp = string[0:k]
            mysplit.append(temp)
            string = string[k:]
        for item in mysplit:
            print(newstring(item))
if __name__ == '__main__':