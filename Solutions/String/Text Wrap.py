import textwrap

def wrap(string, max_width):
    a = []
    for item in string:
        a.append(item)
    while len(a) >= max_width:
        print(''.join(a[0:max_width]))
        a = a[max_width:]
    return ''.join(a[0:len(a)])

if __name__ == '__main__':