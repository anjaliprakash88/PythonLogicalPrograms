num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
vowels = ["a", "e", "i", "o", "u"]
consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
num1=[]
consonant1 = []
vowels1 =[]
x = "hello123"
x1 = x.lower()
for i in x1:
    if i in num:
        num1.append(i)
    elif i in consonant:
        consonant1.append(i)
    elif i in vowels:
        vowels1.append(i)
print("num :", len(num1))
print("consonant:", len(consonant1))
print("vowels:", len(vowels1))