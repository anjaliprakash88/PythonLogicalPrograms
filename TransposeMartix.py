<<<<<<< HEAD
A = [[1, 2, 3],
     [4, 5, 6]]

T = [[0, 0],
     [0, 0],
     [0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        T[j][i] = A[i][j]

        
for i in T:
=======
A = [[1, 2, 3],
     [4, 5, 6]]

T = [[0, 0],
     [0, 0],
     [0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        T[j][i] = A[i][j]

        
for i in T:
>>>>>>> 7139c4579c85c35b896b6146dcf0799b485ae836
    print(i)