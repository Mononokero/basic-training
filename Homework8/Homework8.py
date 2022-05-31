import random
all_height = [random.randint(160, 200) for i in range(10)]
print(all_height)
all_height.sort(reverse=True)
print(all_height)
petia_height = int(input("Petia height=:"))
index = len(all_height) + 1
for i in range(len(all_height)):
    if petia_height > all_height[i]:
        index = i + 1
        break
print(index)
all_height.insert(index -1, "petia_height")
print(all_height)