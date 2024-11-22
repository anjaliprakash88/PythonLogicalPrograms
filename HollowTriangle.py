N = int(input("Enter the Number: "))
for i in range(0, N):
    for s in range(0, N-i-1):
        print(end=" ")
    for j in range(0, i+1):
        if (i >= 2 and i < N-1) and (j > 0 and j < i):
            print(" ", end=" ")
        else:
            print('*', end=" ")
    print()
