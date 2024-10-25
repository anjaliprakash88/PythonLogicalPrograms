<<<<<<< HEAD
# Sum of Natural Numbers Using Recursion
def naturalNumber(n):
    if n == 1:
        return n
    else:
        return n + naturalNumber(n-1)


n = int(input("enter a number: "))
if n <= 0:
    print("enter a +ve number....")
else:
=======
# Sum of Natural Numbers Using Recursion
def naturalNumber(n):
    if n == 1:
        return n
    else:
        return n + naturalNumber(n-1)


n = int(input("enter a number: "))
if n <= 0:
    print("enter a +ve number....")
else:
>>>>>>> 7139c4579c85c35b896b6146dcf0799b485ae836
    print("sum of n natural number is ", naturalNumber(n))