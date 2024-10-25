# Given a string s, find its first non-repeating character and return its index. If it does not exist, return -1.
# Example 1:
# Input: s = "leetcode"

# Output: 0
# Explanation: The first unique character is 'l', which appears at index 0.
a = input("Enter the string: ")

d={}

for i in a:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
length = len(a)
index = 0
result = -1

while index < length:
    letter = a[index]

    value = d[letter]
    if value == 1:
        result = index
        break

    index += 1

print(result)

