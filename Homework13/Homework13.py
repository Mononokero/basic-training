a = 123405
b = 999
c = 1000
d = 1111
def checkio(numbers):
    num = 1
    for i in str(numbers):
        if i == "0":
            num *= 1
        else:
            num *= int(i)
    return num
if __name__ == '__main__':
    print("Prod_a:\n", checkio(a))
    print("Prod_b:\n", checkio(b))
    print("Prod_c:\n", checkio(c))
    print("Prod_d:\n", checkio(d))

