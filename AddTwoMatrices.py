<<<<<<< HEAD
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(A)):
    for j in range(len(A[i])):
        result[i][j] = A[i][j] + B[i][j]

for r in result:
    print(r)

=======
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(A)):
    for j in range(len(A[i])):
        result[i][j] = A[i][j] + B[i][j]

for r in result:
    print(r)

>>>>>>> 7139c4579c85c35b896b6146dcf0799b485ae836