# Stars '*' in A Shape
# for row in range(7):
#     for col in range(5):
#         if ((col == 0 or col == 4) and row != 0) or ((row == 0 or row == 3) and (0 < col < 4)):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# ---------------------------------------------------------------------------------------------------- #
# Stars '*' in B Shape
# for row in range(7):
#     for col in range(5):
#         if col == 0 or (col == 4 and (row != 0 and row != 3 and row != 6)) or (row == 0 or row == 3 or row == 6) and (col > 0 and col < 4):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# ------------------------------------------------------------------------------------------------------ #
# # Stars '*' in C Shape
# for row in range(7):
#     for col in range(5):
#         if (col == 0  and (row != 0 and  row != 6)) or (row == 0 or  row == 6) and (col > 0 and col < 4):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# ------------------------------------------------------------------------------------------------------ #
# # Stars '*' in D Shape
# for row in range(7):
#     for col in range(5):
#         if col == 0 or (col == 4 and (row != 0 and  row != 6)) or (row == 0 or row == 6) and (col > 0 and col < 4):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# ---------------------------------------------------------------------------------------------------- #
# # Stars '*' in E Shape
# for row in range(7):
#     for col in range(5):
#         if col == 0 or (row == 0 or row == 3 or row == 6):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # ---------------------------------------------------------------------------------------------------- #
# # Stars '*' in F Shape
# for row in range(7):
#     for col in range(5):
#         if col == 0 or (row == 0 or row == 3):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# ---------------------------------------------------------------------------------------------------- #
# # Stars '*' in H Shape
# for row in range(7):
#     for col in range(5):
#         if col == 0 or col == 4  or row == 3:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# ---------------------------------------------------------------------------------------------------- #
# # Stars '*' in I Shape
# for row in range(7):
#     for col in range(5):
#         if col == 2 or (row == 0  or row == 6):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# ---------------------------------------------------------------------------------------------------- #
# # Stars '*' in k Shape
# i = 0
# j = 4
# for row in range(7):
#     for col in range(5):
#         if col == 0 or (row == col+2 and col>1):
#             print("*", end=" ")
#         elif ((row == i and col == j) and col > 0):
#             print("*", end="")
#             i = i+1
#             j = j-1
#         else:
#             print(" ", end=" ")
#     print()

# ---------------------------------------------------------------------------------------------------- #
# # Stars '*' in L Shape
# for row in range(7):
#     for col in range(6):
#         if col == 0 or row == 6:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# ---------------------------------------------------------------------------------------------------- #
# # Stars '*' in M Shape
# for row in range(5):
#     for col in range(5):
#         if col == 0 or col == 4 or row == 1 and col == 1 or row == 2 and col == 2 or row == 1 and col == 3:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# ---------------------------------------------------------------------------------------------------- #
# # Stars '*' in N Shape
# for row in range(5):
#     for col in range(5):
#         if col == 0 or col == 4:
#             print("*", end=" ")
#         elif col == row:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# ---------------------------------------------------------------------------------------------------- #
# # Stars '*' in o Shape
# for row in range(5):
#     for col in range(5):
#         if (col == 0 and (row != 0 and row != 4) or
#                 (col == 4 and (row != 4 and row != 0))):
#             print("*", end=" ")
#         elif (row == 0 and (col != 0 and col != 4) or
#               (row == 4 and (col != 4 and col != 0))):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# -------------------------------------------------------------------------
# # Stars '*' in p Shape
# for row in range(7):
#     for col in range(5):
#         if col == 0 or (col == 4 and (row == 1 or row == 2)) or (row == 0 or row == 3) and (col > 0 and col < 4):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# ---------------------------------------------------------------------------------------------------- #
# # Stars '*' in Q Shape
# for row in range(8):
#     for col in range(5):
#         if ((col == 0 or col == 4) and (row > 0 and row < 6)) or ((row == 0 or row == 6) and  (col >0 and col < 4)) or (row == 5 and col==1) or (row == 7 and col == 3):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()


# -------------------------------------------------------------------------
# # Stars '*' in R Shape
# for row in range(7):
#     for col in range(5):
#         if col == 0 or (col == 4 and (row == 1 or row == 2)) or (row == 0 or row == 3) and (col > 0 and col < 4):
#             print("*", end=" ")
#         elif (row == 4 and col == 2) or (row == 5 and col == 3) or (row == 6 and col ==4):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# -------------------------------------------------------------------------
# # Stars '*' in S Shape
# for row in range(7):
#     for col in range(4):
#         if (row == 0 and col != 0) or (row == 6 and col != 3):
#             print("*", end=" ")
#         elif (col == 0 and (row == 1 or row == 2)) or (col == 3 and (row == 4 or row == 5)) or (row == 3 and (col == 1 or col == 2)):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# -------------------------------------------------------------------------
# # Stars '*' in T Shape
# for row in range(5):
#     for col in range(5):
#         if row == 0 or col == 2:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# -------------------------------------------------------------------------
# # # Stars '*' in U Shape
# for row in range(5):
#     for col in range(5):
#         if (col == 0 or col == 4) and row != 4:
#             print("*", end=" ")
#         elif row == 4 and (col > 0 and col < 4):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# -------------------------------------------------------------------------
# # Stars '*' in V Shape
# for row in range(4):
#     for col in range(7):
#         if col == row:
#             print("*", end=" ")
#         elif (row == 0 and col == 6) or (row == 1 and col == 5) or (row == 2 and col == 4):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# -------------------------------------------------------------------------
# # Stars '*' in W Shape
# for row in range(4):
#     for col in range(11):
#         if col == row or (row == 0 and col == 10):
#             print("*", end=" ")
#         elif (row == 1 and (col == 5 or col == 9)) or (row == 2 and col == 4):
#             print("*", end=" ")
#         elif (row == 2 and (col == 6 or col == 8)) or (row == 3 and (col == 7 )):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# -------------------------------------------------------------------------
# # Stars '*' in X Shape
# for row in range(5):
#     for col in range(5):
#         if col == row:
#             print("*", end=" ")
#         elif (row == 4 and col == 0) or (row == 3 and col == 1) or (row == 1 and col == 3) or (row == 0 and col == 4):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# -------------------------------------------------------------------------
# Stars '*' in Y Shape
for row in range(5):
    for col in range(5):
        if (row == 0 and col == 0) or (row == 1 and col == 1) or (row == 2 and col == 2):
            print("*", end=" ")
        elif (row == 4 and col == 0) or (row == 3 and col == 1) or (row == 1 and col == 3) or (row == 0 and col == 4):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()