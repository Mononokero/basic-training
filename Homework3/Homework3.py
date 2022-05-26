c1 = int(input("Input 1st class pupils count:\n"))
result = (c1)
print("result:", c1, type(result))

c2 = int(input("Input 12nd class pupils count:\n"))
result = (c2)
print("result:", c2, type(result))

c3 = int(input("Input 13rd class pupils count:\n"))
result = (c3)
print("result:", c3, type(result))

r = int(3)
print("Class_rooms _count =", r, type(r))

d1= (c1 // 2)  + (c1 % 2)
print("1st class desk count=", d1,  type(d1))

d2 = (c2 // 2) + (c2 % 2)
print("2nd class desk count=", d2, type(d2))

d3 = (c3 // 2) + (c3 % 2)
print("3rd class desk count=", d3, type(d3))

sum = str("All clssses desk sum=")
result = (d1 + d2 +d3)
print(sum, result, type(result))

