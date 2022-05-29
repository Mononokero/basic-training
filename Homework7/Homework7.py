rows = int(input("Input row count:"))
for iter_step in range(0, rows):
    for init_state in range(0, rows - iter_step - 1):
        print("  ", end="  ")
    for init_state in range(iter_step * 2 + 1):
        print(' * ', end=" ")
    print("\n")
