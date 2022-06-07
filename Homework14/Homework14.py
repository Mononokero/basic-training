import math

a = 5
def square(a):
    s = a * a
    p = a * 4
    d = a * math.sqrt(2)
    result = (s, p, d)
    return result

print(square(a))