<<<<<<< HEAD
def check(x):
    x = x.lower()
    vowel = set("aeiou")
    s = set({})
    for char in x:
        if char in vowel:

            s.add(char)
        else:
            pass
    if len(s) == len(vowel):
        print("string contains all vowels")
    else:
        print("string does not contains all vowles")


x = input("enter the string")
check(x)
=======
def check(x):
    x = x.lower()
    vowel = set("aeiou")
    s = set({})
    for char in x:
        if char in vowel:
            s.add(char)
        else:
            pass
    if len(s) == len(vowel):
        print("string contains all vowels")
    else:
        print("string does not contains all vowles")


x = input("enter the string")
check(x)
>>>>>>> 7139c4579c85c35b896b6146dcf0799b485ae836
