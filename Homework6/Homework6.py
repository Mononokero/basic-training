number = int(input("Input any number:"))
count = 0
sum = 0
min = max = number
even = 0
odd = 0
while number != 0:
    count += 1
    sum += number
    if number > max:
       max = number
    if number < min:
       min = number
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
    number = int(input("Input any number:"))
print("Amount:", count)
print("Sum input numbers", sum)
print("Average", (sum / count))
print(f'max = {max} \ min = {min}')
print("Odd", odd, "Even", even)
