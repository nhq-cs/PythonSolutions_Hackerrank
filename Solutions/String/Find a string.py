def count_substring(string, sub_string):
    count = 0
    index = len(sub_string)
    for i in range(len(string) - index +1):
        if string[i:i+index] == sub_string:
            count +=1
    return  count

if __name__ == '__main__':