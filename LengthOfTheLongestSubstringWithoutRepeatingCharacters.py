<<<<<<< HEAD
s = "bbbbb"
demo = []
max_length = 0
start = 0

for i in range(len(s)):
    while s[i] in demo:
        demo.pop(0)
        start += 1
    demo.append(s[i])
    max_length = max(max_length, len(demo))

print(max_length) 
=======
s = "bbbbb"
demo = []
max_length = 0
start = 0

for i in range(len(s)):
    while s[i] in demo:
        demo.pop(0)
        start += 1
    demo.append(s[i])
    max_length = max(max_length, len(demo))

print(max_length) 
>>>>>>> 7139c4579c85c35b896b6146dcf0799b485ae836
