# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# rows = 6
# for i in range(rows):
#     for j in range(i):
#         print(i, end=' ')
#     print('')

# --------------------------------------
#     1
#   3 3 3
#  5 5 5 5 5
# 7 7 7 7 7 7 7
# n=4
# for i in range(1,n+1):
#     print("  " * (n - i), end=" ")
#     for j in range(2*i-1):
#         print(2*i-1, end=" ")
#     print()

# ---------------------------------

# A
# B C
# D E F
# G H I J
# K L M N O
# n = int(input("enter number of rows"))
# x = ord("A")
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(chr(x), end=' ')
#         x = x + 1
#     print()

# -------------------------------------------
# A
# A B
# A B C
# A B C D
# A B C D E
# for i in range(65, 70):
#     for j in range(65, i+1):
#         print(chr(j), end=' ')
#     print()

# --------------------------------
# *
# * *
# * * *
# * * * *
# * * * * *
# n = int(input("enter number of rows"))
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=' ')
#     print()

# -------------------------------------
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# n = int(input("enter number of rows"))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()

# ---------------------------------
# *
# * * *
# * * * * *
# * * * * * * *
# * * * * * * * * *
# n = int(input("enter number of rows"))
# k = 1
# for i in range(1, n+1):
#     for j in range(1, k+1):
#         print("*", end=' ')
#     k = k + 2
#     print()

# ---------------------------------------
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# n = int(input("enter number of rows"))
# for i in range(0, n):
#     for j in range(0, n-i-1):
#         print(end=" ")
#     for j in range(0, i+1):
#         print("*", end=" ")
#     print()

#--------------------------------------

#            1
#          3  5
#        7  9  11
#    13  15  17   19
#  21  23  25  27  29

# n = int(input("Enter the number of rows: "))
# num = 1
#
# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end=" ")
#
#     for j in range(i + 1):
#         print(num , end=" ")
#         num += 2
#     print()


# -------------------------------------------

# *  *  *  *  *
#   *  *  *  *
#    *  *  *
#      *  *
#        *

# n = int(input("Enter the number of rows: "))
#
# for i in range(n, 0, -1):
#     for j in range(0, n-i):
#         print(end=" ")
#
#     for j in range(0, i):
#         print("*", end=" ")
#
#     print()

# -------------------------------------------
#         *
#       *  *
#     *  *  *
#   *  *  *  *
# *  *  *  *  *
#   *  *  *  *
#    *  *  *
#      *  *
#        *
n = int(input("enter number of rows"))
for i in range(0, n-1):
    for j in range(0, n-i-1):
        print(end=" ")
    for j in range(0, i+1):
        print("*", end=" ")
    print()

for i in range(n, 0, -1):
    for j in range(0, n-i):
        print(end=" ")

    for j in range(0, i):
        print("*", end=" ")

    print()