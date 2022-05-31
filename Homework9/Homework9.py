import random
any_list = [random.randint(16, 53) for i in range(10)]
for i , e in enumerate(any_list):
    print( f'Index {i} for {e}')
greater_then_neighbors = 0
for i in range(1, 8):
    if int(any_list[i-1]) < (any_list[i]) and (any_list[i]) > int(any_list[i+1]):
        greater_then_neighbors += 1
print("Greater_then_neighbors:", greater_then_neighbors)
print(any_list)
