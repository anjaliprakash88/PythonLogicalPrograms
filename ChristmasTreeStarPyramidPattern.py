n = int(input("Enter the number of rows for the tree: "))

# Loop for the top part of the tree
for i in range(0, n):
    for j in range(0, n - i - 1):
        print(" ", end="")  # Add spaces for alignment
    for j in range(0, i + 1):
        print("* ", end="")  # Print stars with a space
    print()

# Loop for the middle part of the tree
for i in range(1, n + 1):
    for j in range(0, n - i - 1):
        print(" ", end="")  # Add spaces for alignment
    for j in range(0, i + 1):
        print("* ", end="")  # Print stars with a space
    print()

# Loop for the bottom part of the tree
for i in range(2, n + 2):
    for j in range(0, n - i - 1):
        print(" ", end="")  # Add spaces for alignment
    for j in range(0, i + 1):
        print("* ", end="")  # Print stars with a space
    print()