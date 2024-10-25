<<<<<<< HEAD
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix+matrix2)

import numpy as np
m1= np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
=======
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix+matrix2)

import numpy as np
m1= np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
>>>>>>> 7139c4579c85c35b896b6146dcf0799b485ae836
print(np.concatenate((m1, m2)))