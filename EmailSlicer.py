<<<<<<< HEAD
def email(x):
    if "@" in x:
        username, domain = x.split("@")
        print("Username:", username)
        print("Domain:", domain)
    else:
        print("Invalid email address format")


x = input("Enter an email address: ")
email(x)
=======
def email(x):
    if "@" in x:
        username, domain = x.split("@")
        print("Username:", username)
        print("Domain:", domain)
    else:
        print("Invalid email address format")

x= input("Enter an email address: ")
email(x)
>>>>>>> 7139c4579c85c35b896b6146dcf0799b485ae836
