string = ("one five one six one")
dictionary = {}
for word in string.split():
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 0
    print(dictionary[word], end=" ")
