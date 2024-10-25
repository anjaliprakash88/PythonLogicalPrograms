<<<<<<< HEAD
items = int(input("enter the number of items that your want to input in array: "))
D = int(input("enter the targeted value: "))
N = []
for i in range(items):
    N.append(int(input("enter the items:")))
print(N)
count = 0
for i in N:
    if i == D:
        count+=1

=======
items = int(input("enter the number of items that your want to input in array: "))
D = int(input("enter the targeted value: "))
N = []
for i in range(items):
    N.append(int(input("enter the items:")))
print(N)
count = 0
for i in N:
    if i == D:
        count+=1

>>>>>>> 7139c4579c85c35b896b6146dcf0799b485ae836
print(count)