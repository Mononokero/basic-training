'''''''''''''''''''''''''''''''''''''''''''''
a = int(input("Input a: \n"))
b = int(input("Input b: \n"))
c = input("Input arithmetic operation: \n")
def arithmetic(a, b, c):
    if c == "+":
      return  a + b
    elif c =="-":
        return a - b
    elif c =="/":
        return a / b
    elif c == "*":
        return a * b
    else:
        return ("Unknown operation")
print("Result:")
print(arithmetic(a, b, c))
'''''''''''''''''''''''''''''''''''''''''''''''

a = int(input("Input a: \n"))
b = int(input("Input b: \n"))
c = input("Input arithmetic operation: \n")
def arithmetic(a, b, c):
    return {
        '+': lambda: a+b,
        '-': lambda: a-b,
        '*': lambda: a*b,
        '/': lambda: a/b,
    }.get(c, lambda: 'Unknown operation')()

print(arithmetic(a, b, c))
