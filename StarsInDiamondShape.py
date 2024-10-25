row = 6
for i in range(0, row-1):
    for j in range(0, row-i-1):
        print(" ", end="")
    for j in range(0, i+1):
        print(" *", end="")
    print()

for i in range(row, 0, -1):
    for j in range(0, row-i+1):
        print(" ", end="")
    for j in range(0, i):
        print("*", end=" ")
    print()