# Write a program to find the first non-repeating character in a given string. If all characters in
# the string repeat, display a message indicating that there are no non-repeating characters.
# Input Format:
# A single string consisting of lowercase English alphabets.
# Output Format:
# The first non-repeating character in the string, or a message stating that no
# non-repeating character was found.
# Example 1:
# Input: swiss
# Output: w

x = "swiswi"
x1 = x.lower()
d = {}

for i in range(len(x1)):
    count = 0
    for j in range(len(x1)):
        if x1[i] == x1[j] and i != j:
            count += 1
    d[x1[i]] = count

for i, j in d.items():
    if j == 0:
        print(i)
        break
else:
    print("No repeating characters")



