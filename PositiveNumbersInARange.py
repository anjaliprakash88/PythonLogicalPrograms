<<<<<<< HEAD
x = [1, -34, 56, -78, 90, -43, 12, -45, 35, -15, 45, -95, 46, -75, 25]
y = []
start = int(input("enter the starting range"))
end = int(input("enter the ending range"))
for i in range(start, end+1):
    if x[i] >= 0:
        y.append(x[i])
=======
x = [1, -34, 56, -78, 90, -43, 12, -45, 35, -15, 45, -95, 46, -75, 25]
y = []
start = int(input("enter the starting range"))
end = int(input("enter the ending range"))
for i in range(start, end+1):
    if x[i] >= 0:
        y.append(x[i])
>>>>>>> 7139c4579c85c35b896b6146dcf0799b485ae836
print(y)