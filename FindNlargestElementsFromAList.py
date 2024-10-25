<<<<<<< HEAD
x = [1, 34, 56, 78, 90, 43, 12, 45, 35]
k = int(input("enter a number"))
if k == len(x):
    print("we cannot find n largest numbers in th list")
else:
    x.sort()
=======
x = [1, 34, 56, 78, 90, 43, 12, 45, 35]
k = int(input("enter a number"))
if k == len(x):
    print("we cannot find n largest numbers in th list")
else:
    x.sort()
>>>>>>> 7139c4579c85c35b896b6146dcf0799b485ae836
    print(x[-k:])