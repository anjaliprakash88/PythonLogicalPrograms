# You are given a list of integers that may contain duplicates. A 'single Number' is defined as a number
# that appears only once in the list. Your task is to find the largest single number in the list. if there is no
# single number, return null

num = [1, 3, 5, 3]
x = []
for i in num:
    if num.count(i) == 1:
        x.append(i)
if len(x) == 0:
    print("Null")
else:
    print(max(x))