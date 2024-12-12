# given a string s, return the string s without any vowels('a', 'e', 'i', 'o', 'u' both in lowercase &
# uppercase
# input: s="hello world"
# output: "hllwrld"
s="hElLo world"
s1=s.lower()
out =""
vowels = "aeiou"
for i in s1:
    if i not in vowels:
        out += i
print(out)
