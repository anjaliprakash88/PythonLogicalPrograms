# Given a positive integer num represented as a string, return the integer num without
# any non-numeric character(such as letters or symbols)
# input: num="12a34b56"
# output: "123456"

num = "12a34b56rtd456723@##$%%"
out =''
n = '1234567890'
for i in num:
    if i in n:
        out += i
print(out)


