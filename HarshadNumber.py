<<<<<<< HEAD
# x = int(input("enter a  number: "))
# temp = x
# sum = 0
# while temp > 0:
#     rem = temp % 10
#     sum += rem
#     temp //= 10
#
# if x%sum == 0:
#     print("Harshad Number")
# else:
#     print("Not Harshad Number")


a =  int(input("Enter the number :"))
b=str(a)
d=0
e=0
for i in range(len(b)):
    c = int(b[i])
    d=d+c
    e=a%d
if e==0:
    print("it is harshad number")
else:
    print("it is not harshad number")
=======
x = int(input("enter a  number: "))
temp = x
sum = 0
while temp > 0:
    rem = temp % 10
    sum += rem
    temp //= 10

if x%sum == 0:
    print("Harshad Number")
else:
    print("Not Harshad Number")


>>>>>>> 7139c4579c85c35b896b6146dcf0799b485ae836
