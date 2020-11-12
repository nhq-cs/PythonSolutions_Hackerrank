def minion_game(string):
    vowels = set('AEUIOU')
    stuart = kevin = 0
    for i,c in enumerate(string):
        if c in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string)- i
    if stuart > kevin:
        print("Stuart", stuart)
    elif stuart == kevin:
        print('Draw')
    else:
        print("Kevin", kevin)
if __name__ == '__main__':