<<<<<<< HEAD
x = "Welcome to Python Program"
y = x.split(" ")  
print(y)

count = 0
longest_word = ""

for i in y:
    length = len(i)
    if count < length:
        count = length
        longest_word = i

=======
x = "Welcome to Python Program"
y = x.split(" ")  
print(y)

count = 0
longest_word = ""

for i in y:
    length = len(i)
    if count < length:
        count = length
        longest_word = i

>>>>>>> 7139c4579c85c35b896b6146dcf0799b485ae836
print(f"The longest word is: '{longest_word}' with length {count}")