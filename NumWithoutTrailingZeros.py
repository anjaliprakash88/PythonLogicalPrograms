# Given a positive integer num represented as a string, return the integer num without trailing zeros as
# a string.
# Example 1:
# Input: num = "51230100"
# Output: "512301"
# Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".

num = "51230100"
count = 0
x = []
for i in range(len(num)-1, -1, -1):
    if num[i] == "0":
        count += 1
    else:
        break
for j in range(len(num) - count):
    x.append(num[j])


x1 = ''.join(x)

x2 = int(x1)
print(type(x2))

