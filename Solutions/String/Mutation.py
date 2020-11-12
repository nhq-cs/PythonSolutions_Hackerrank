def mutate_string(string, position, character):
    temp = list(string)
    temp[position] = character
    string = ''.join(temp)
    return  string

if __name__ == '__main__':