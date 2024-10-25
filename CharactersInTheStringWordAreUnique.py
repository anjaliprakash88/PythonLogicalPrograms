<<<<<<< HEAD
x = "hello"
l = []
flag = True
for i in x:
    if i not in l:
        l.append(i)
    else:
        flag = False
        break
if flag:
    print("Given word is Unique")
else:
=======
x = "python"
l = []
flag = True
for i in x:
    if i not in l:
        l.append(i)
    else:
        flag = False
        break
if flag:
    print("Given word is Unique")
else:
>>>>>>> 7139c4579c85c35b896b6146dcf0799b485ae836
    print("Given word is not Unique")