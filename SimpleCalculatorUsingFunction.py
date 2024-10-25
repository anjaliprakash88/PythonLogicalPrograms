<<<<<<< HEAD
def add(x, y):
    return x + y


def substract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("select Operation")
print(" 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")
while True:
    choice = input("enter your choice")
    if choice in ("1", "2", "3", "4"):
        num1 = float(input("Enter a Number: "))
        num2 = float(input("Enter a Number: "))
        if choice == "1":
            print(add(num1, num2))
        elif choice == "2":
            print(substract(num1, num2))
        elif choice == "3":
            print(multiply(num1, num2))
        elif choice == "4":
            print(divide(num1, num2))
        elif choice == "5":
            exit()
        else:
            print("Invalid")
=======
def add(x, y):
    return x + y


def substract(x, y):
    return x + y


def multiply(x, y):
    return x + y


def divide(x, y):
    return x + y


print("select Operation")
print("1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")
while True:
    choice = input("enter your choice"
                   "")
>>>>>>> 7139c4579c85c35b896b6146dcf0799b485ae836
