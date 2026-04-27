# #2 variables
# a=int(input("enter: "))
# b=int(input("enter: "))
# c=a
# a=b
# b=c
# print("a:",a,"b:",b)

# #3 variables
# a=int(input("enter: "))
# b=int(input("enter: "))
# c=int(input("enter: "))
# d=a
# a=b
# b=c
# c=d
# print("a:",a,"b:",b,"c:",c)

# #3 variables reverse swap
# a=int(input("enter: "))
# b=int(input("enter: "))
# c=int(input("enter: "))
# d=a
# a=c
# b=b
# c=d
# print("a:",a,"b:",b,"c:",c)

# #2 variables swap
# a=int(input("enter: "))
# b=int(input("enter: "))
# a,b=b,a
# print("a:",a,"b:",b)

# #2 variables swap
# a=int(input("enter: "))
# b=int(input("enter: "))
# a=a+b #2,3=5
# b=a-b #5,3=2
# a=a-b #5,2=3
# print("a:",a,"b:",b)

# #3 variables swap
# a=int(input("enter: "))
# b=int(input("enter: "))
# c=int(input("enter: "))
# a=a+b+c #2,3,4=9
# b=a-b-c #9,3,4=2
# c=a-b-c #9,2,4=3
# a=a-b-c #9,2,3=4
# print("a:",a,"b:",b,"c:",c)

# #find reminder without modulus
# a=int(input("enter: "))
# b=int(input("enter: "))
# c=a%b
# print("output:",c)
# c1=a//b
# print("output:",c1)
# c2=a-(c1*b)
# print("output:",c2)

# #abs
# a=int(input("enter: "))
# print(abs(a))
# #without abs
# print((a**2)**0.5)
# #without abs 2
# import math
# a1=pow(a,2)
# print(math.sqrt(a1))

# #find last digit
# a=int(input("enter: "))
# b1=a%10
# print("last digit:",b1)

# #find first digit
# a=int(input("enter: "))
# b=a//1000
# print("first digit:",b)

# #find second digit
# a=int(input("enter: "))
# b1=a%1000
# b2=b1//100
# print("second digit:",b2)

# #find third digit
# a=int(input("enter: "))
# b1=a%100
# b2=b1//10
# print("second digit:",b2)

# #reverse the number
# a=int(input("enter: ")) #1234
# b=(a%10)*1000
# c=a%100
# c1=(c//10)*100
# d=a%1000
# d1=(d//100)*10
# e=(a//1000)*1
# print(b,c1,d1,e)
# print(b+c1+d1+e)
