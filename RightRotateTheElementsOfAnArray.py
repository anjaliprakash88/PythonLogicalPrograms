<<<<<<< HEAD
arr = [1, 2, 3, 4, 5]
n = len(arr)
k = 3

for j in range(k):
    last_element = arr[-1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last_element

print(arr)
=======
arr = [1, 2, 3, 4, 5]
n = len(arr)
k = 3

for j in range(k):
    last_element = arr[-1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last_element

print(arr)
>>>>>>> 7139c4579c85c35b896b6146dcf0799b485ae836
