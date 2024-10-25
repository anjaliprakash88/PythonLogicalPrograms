<<<<<<< HEAD
def find_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    hcf = 1
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i

    return hcf

print(find_hcf(55, 65))
=======
def find_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    hcf = 1
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i

    return hcf

print(find_hcf(55, 65))
>>>>>>> 7139c4579c85c35b896b6146dcf0799b485ae836
