# Given an integer num, repeatedly add all its digits until the result has only one digit and return it.
# input: 38
# output: 2

num = 1000
while num > 10:
    sum = 0
    x = str(num)
    for i in x:
        sum = sum + int(i)
    num = sum

print(num)