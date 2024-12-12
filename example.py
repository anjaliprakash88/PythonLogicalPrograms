x = [1, 6, 1, 73, 56]
y = []
for i in range(max(x)+1):
    if i in x:
        y.append(i)
print(y[-2])
