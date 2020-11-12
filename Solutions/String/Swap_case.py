def swap_case(s):
    temp  = ''
    for i in range(len(s)):
        if s[i].isupper() == True:
            temp += s[i].lower()
        else:
            temp += s[i].upper()

    return temp

if __name__ == '__main__':