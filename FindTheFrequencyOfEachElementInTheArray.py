<<<<<<< HEAD
arr = [1, 2, 2, 8, 3, 5, 2, 2, 1]
frequency = {}

for element in arr:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1

print("----------------------------------------")
print("Element     | Frequency")
print("----------------------------------------")
for key, value in frequency.items():
    print(key, "          |",      value)
print("----------------------------------------")
=======
arr = [1, 2, 2, 8, 3, 5, 2, 2, 1]
frequency = {}

for element in arr:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1

print("----------------------------------------")
print("Element     | Frequency")
print("----------------------------------------")
for key, value in frequency.items():
    print(key, "          |",      value)
print("----------------------------------------")
>>>>>>> 7139c4579c85c35b896b6146dcf0799b485ae836
