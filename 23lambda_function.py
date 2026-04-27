##### lambda function
# Python Lambda Functions are anonymous functions, meaning functions without a name. Normally, we use the 'def' keyword to define a function, but for anonymous functions, we use the 'lambda' keyword.

# # Program 1
# str1="hi i am jaga"
# upper=lambda str2:str1.upper()
# print(upper(str1))

# # Program 2
# sum=lambda a,b:a+b
# x=int(input("enter: "))
# y=int(input("enter: "))
# z=sum(x,y)
# print(sum(x,y))
# print("sum =",z)

# # 1. Area of triangle → A = √(s*(s−a)*(s−b)*(s−c))
# import math
# Area_of_triangle=lambda s,a,b,c:math.sqrt(s*(s-a)*(s-b)*(s-c))
# s=int(input("enter: "))
# a=int(input("enter: "))
# b=int(input("enter: "))
# c=int(input("enter: "))
# print(Area_of_triangle(s,a,b,c))

# # 2. Perimeter of triangle → P = a + b + c
# perimeter_of_triangle=lambda a,b,c:a+b+c
# a=int(input("enter: "))
# b=int(input("enter: "))
# c=int(input("enter: "))
# print(perimeter_of_triangle(a,b,c))

# # 3. Area of Equilateral triangle → A = a²
# area_of_equilateral_triangle=lambda a:pow(a,2)
# a=int(input("enter: "))
# print(area_of_equilateral_triangle(a))

# # Program 3
# big=lambda a,b:print("a is big") if (a>b) else print("b is big")
# a=int(input("enter: "))
# b=int(input("enter: "))
# big(a,b)

# # Program 4
# power=lambda l:[i**2 for i in l]
# l=[2,4,6,8]
# print(power(l))

# # a) Biggest of Three Numbers
# big=lambda a,b,c:print("a is big") if (a>b) and (a>c) else print("b is big") if (b>c) else print("c ic big")
# a=int(input("enter: "))
# b=int(input("enter: "))
# c=int(input("enter: "))
# big(a,b,c)

# # b) Smallest of Three Numbers
# small=lambda a,b,c:print("a is small") if (a<b) and (a<c) else print("b is small") if (b<c) else print("c is small")
# a=int(input("enter: "))
# b=int(input("enter: "))
# c=int(input("enter: "))
# small(a,b,c)

# # c) Biggest of Four Numbers
# big=lambda a,b,c,d:print("a is big") if (a>b and a>c and a>d) else print("b is big") if (b>c and b>d) else print("c is big") if (c>d) else print("d is big")
# a=int(input("enter: "))
# b=int(input("enter: "))
# c=int(input("enter: "))
# d=int(input("enter: "))
# big(a,b,c,d)

# # d) Smallest of Four Numbers
# small=lambda a,b,c,d:print("a is small") if (a<b and a<c and a<d) else print("b is small") if (b<c and b<d) else print("c is small") if (c<d) else print("d is small")
# a=int(input("enter: "))
# b=int(input("enter: "))
# c=int(input("enter: "))
# d=int(input("enter: "))
# small(a,b,c,d)

# # e) Students Marklist
# grade=lambda tam,eng,math,che,phy,avg:print("fail") if (tam<35 and eng<35 and math<35 and che<35 and phy<35) else print('Grade is O') if(avg>90) else print('Grade is A') if(avg>75) else print('Grade is B') if(avg>50) else print('fail')
# name=str(input("enter name:"))
# roll_no=int(input("enter rool_no:"))
# tam=int(input("enter tam:"))
# eng=int(input("enter eng:"))
# math=int(input("enter math:"))
# che=int(input("enter che:"))
# phy=int(input("enter phy:"))
# total=tam+eng+math+che+phy
# avg=total/5
# print('Name=', name)
# print('Roll No: ', roll_no)
# print('Total: ', total)
# grade(tam,eng,math,che,phy,avg)

# # f) Sales Commission
# com=lambda sale:print((sale*0)//100) if(sale<10000) else print((sale*5)//100) if(sale<20000) else print((sale*10)//100) if(sale<50000) else print((sale*15)//100) if(sale<100000) else print((sale*20)//100+500) if(sale>100000) else print('invalid')
# sale=int(input('Enter sales'))
# com(sale)

# # g) Tax Calculation
# tax=lambda x: x*0/100 if(x<10000) else ((x-10000)*10/100)if(x<20000) else ((x-20000)*20//100+(10000*10//100)) if(x>=20000) else 'invalid'
# x=int(input('Enter tax'))
# z=tax(x)
# print('Tax: ',z)

# # h) Electricity Bill
# eb=lambda unit:(unit*1.2) if(unit<200) else ((unit-199)*1.5+(199*1.2)) if(unit<400) else ((unit-399)*1.8+(199*1.2)+(200*1.5)) if(unit<500) else ((unit-599)*2+(199*1.2)+(200*1.5)+(200*1.8)) if(unit>599) else 'sorry'
# unit=int(input('Enter unit'))
# z=eb(unit)
# if(z>400):
#     sur=(z*15//100)
#     z=sur+z
# print(z)





