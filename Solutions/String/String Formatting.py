def print_formatted(number):
    def octal(number):
        string = oct(number)
        return string[2:]
    def hexa(number):
        string = hex(number)
        return string[2:].upper()
    def bina(number):
        string = bin(number)
        return string[2:]
    for i in range(1,number+1):
        print(i, octal(i), hexa(i), bina(i))
if __name__ == '__main__':