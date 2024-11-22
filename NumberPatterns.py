# 12345
# 1234
# 123
# 12
# 1
# row = int(input("Enter a number: "))
# for i in range(row, 0, -1):
#     count = 1
#     for j in range(i):
#         print(count, end="")
#         count = count+1
#     print()


# ----------------------------------------
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
row = int(input("Enter a number: "))
for i in range(row, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()
