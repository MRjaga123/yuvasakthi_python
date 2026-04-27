# #string intupts
# a=str(input("enter a: "))
# b=str(input("enter b: "))
# c=str(input("enter c: "))
# d=str(input("enter d: "))
# e=str(input("enter e: "))
# print(a,b,c,d,e)

###if statements
# #odd or even
# a=int(input("enter a: "))
# if a%2==0:
#     print(f"a {a} is even number")
# if a%2!=0:
#     print(f"a{a} is odd number")

# #biggest number
# a=int(input("enter a: "))
# b=int(input("enter b: "))
# if a>b:
#     print(f"a {a} is big number")
# if b>a:
#     print(f"b {b} is big number")

# #smallest number
# a=int(input("enter a: "))
# b=int(input("enter b: "))
# if a<b:
#     print(f"a {a} is small number")
# if b<a:
#     print(f"b {b} is small number")

# #positive or negative number
# a=str(input("enter a: "))
# if "+" in a:
#     print(f"a {a} is positive number")
# if "-" in a:
#     print(f"a {a} is negative number")
# if "+" or "-" not in a:
#     print(f"a {a} is normal number")

# #age eligible for vote
# a=int(input("enter age: "))
# if a>=18:
#     print(f"age {a} is eligible for vote")
# if a<18:
#     print(f"age {a} is not eligible for vote")

# #find profit or loss
# invest=int(input("enter costs: "))
# returns=int(input("enter returns: "))
# if invest<returns:
#     print(f"{returns-invest} is a profit")
# if invest>returns:
#     print(f"{returns-invest} is a loss")

# #triangle
# a=int(input("enter a: "))
# b=int(input("enter b: "))
# c=int(input("enter c: "))
# if (a+b+c)==180:
#     print(f"{a+b+c} is a triangle")
# if (a+b+c)!=180:
#     print(f"{a+b+c} is not a triangle")

# #absolute value
# num=int(input("enter num: "))
# if num == abs(num):
#     print(f"{num} is a absolute positive number")
# if num != abs(num):
#     print(f"{num} is not a absolute positive number, so i changed to {abs(num)} absolute positive number ")


# ##if_else
# #odd or even
# a=int(input("enter a: "))
# if a%2==0:
#     print(f"a {a} is even number")
# else:
#     print(f"a{a} is odd number")

# #biggest number
# a=int(input("enter a: "))
# b=int(input("enter b: "))
# if a>b:
#     print(f"a {a} is big number")
# else:
#     print(f"b {b} is big number")

# #smallest number
# a=int(input("enter a: "))
# b=int(input("enter b: "))
# if a<b:
#     print(f"a {a} is small number")
# else:
#     print(f"b {b} is small number")

# #positive or negative number
# a=str(input("enter a: "))
# if "+" in a:
#     print(f"a {a} is positive number")
# else:
#     print(f"a {a} is negative number")


# #age eligible for vote
# a=int(input("enter age: "))
# if a>=18:
#     print(f"age {a} is eligible for vote")
# else:
#     print(f"age {a} is not eligible for vote")

# #find profit or loss
# invest=int(input("enter costs: "))
# returns=int(input("enter returns: "))
# if invest<returns:
#     print(f"{returns-invest} is a profit")
# else:
#     print(f"{returns-invest} is a loss")

# #triangle
# a=int(input("enter a: "))
# b=int(input("enter b: "))
# c=int(input("enter c: "))
# if (a+b+c)==180:
#     print(f"{a+b+c} is a triangle")
# else:
#     print(f"{a+b+c} is not a triangle")

# #absolute value
# num=int(input("enter num: "))
# if num == abs(num):
#     print(f"{num} is a absolute positive number")
# else:
#     print(f"{num} is not a absolute positive number, so i changed to {abs(num)} absolute positive number ")


# ##if_elif_else
# #find biggest number
# a=int(input("enter a: "))
# b=int(input("enter b: "))
# c=int(input("enter c: "))
# if a>b and a>c:
#     print(f"{a} is a biggest number")
# elif b>a and b>c:
#     print(f"{b} is b biggest number")
# else:
#     print(f"{c} is c biggest number")

# #find smallest number
# a=int(input("enter a: "))
# b=int(input("enter b: "))
# c=int(input("enter c: "))
# if a<b and a<c:
#     print(f"{a} is a smallest number")
# elif b<a and b<c:
#     print(f"{b} is b smallest number")
# else:
#     print(f"{c} is c smallest number")

# #find postive or nagative or neutral number
# num=str(input("enter num: "))
# if "+" in num:
#     print(f"{num} is num positive number")
# elif "-" in num:
#     print(f"{num} is num negative number")
# else:
#     print(f"{num} is num neutral number")

# #find child, adult or senior citizen for given age
# age=int(input("enter age: "))
# if age>0 and age < 18:
#     print(f"{age} age is a child ")
# elif age>=18 and age<60:
#     print(f"{age} age is a adult ")
# else:
#     print(f"{age} age is a senoir citizen")

# #arithmetic functions
# num1=int(input("enter num1: "))
# num2=int(input("enter num2: "))
# operator=str(input("enter operator: "))
# if operator == "+":
#     print(f"num1+num2= {num1+num2}")
# elif operator == "-":
#     print(f"num1-num2= {num1-num2}")
# elif operator == "*":
#     print(f"num1*num2= {num1*num2}")
# elif operator == "/":
#     print(f"num1/num2= {num1/num2}")
# else:
#     print(f"invalid operator {operator}")

# #find the temperature
# temp=int(input("enter the temp: "))
# if temp<0:
#     print(f"{temp} is freezing")
# elif temp>=0 and temp<10:
#     print(f"{temp} is very cold")
# elif temp>=10 and temp<20:
#     print(f"{temp} is cold")
# elif temp>=20 and temp<30:
#     print(f"{temp} is normal")
# elif temp>=30 and temp<=40:
#     print(f"{temp} is hot")
# else:
#     print(f"{temp} is very hot")

# #equivalent day
# day=int(input("enter the day: "))
# if day == 1:
#     print(f"{day} is sunday")
# elif day == 2:
#     print(f"{day} is monday")
# elif day == 3:
#     print(f"{day} is tuesday")
# elif day == 4:
#     print(f"{day} is wednesday")
# elif day == 5:
#     print(f"{day} is thursday")
# elif day == 6:
#     print(f"{day} is friday")
# elif day == 7:
#     print(f"{day} is saturday")
# else:
#     print(f"{day} is invalid day")

# #equivalent month
# month=int(input("enter the month: "))
# if month == 1:
#     print(f"{month} is jan")
# elif month == 2:
#     print(f"{month} is feb")
# elif month == 3:
#     print(f"{month} is mar")
# elif month == 4:
#     print(f"{month} is apr")
# elif month == 5:
#     print(f"{month} is may")
# elif month == 6:
#     print(f"{month} is jun")
# elif month == 7:
#     print(f"{month} is jul")
# elif month == 8:
#     print(f"{month} is ags")
# elif month == 9:
#     print(f"{month} is sep")
# elif month == 10:
#     print(f"{month} is oct")
# elif month == 11:
#     print(f"{month} is nov")
# elif month == 12:
#     print(f"{month} is dec")
# else:
#     print(f"{month} is invalid month")

# #find the no of days in month
# month=int(input("enter the month: "))
# if month==1 or month ==3 or month ==5 or month ==7 or month ==8 or month ==10 or month ==12:
#     print(f"{month} has 31 days")
# elif month==4 or month ==6 or month ==9 or month ==11:
#     print(f"{month} has 30 days")
# elif month == 2:
#     print(f"{month} has 28 days")
# else:
#     print(f"{month} is invalid")

# #find student grade
# mark1=int(input("enter the mark1: "))
# mark2=int(input("enter the mark2: "))
# mark3=int(input("enter the mark3: "))
# mark4=int(input("enter the mark4: "))
# mark5=int(input("enter the mark5: "))
# if (mark1>=35 and mark2>=35 and mark3>=35 and mark4>=35 and mark5>=35) and (mark1<=50 and mark2<=50 and mark3<=50 and mark4<=50 and mark5<=50):
#     print("grade is 'C'")
# elif (mark1>50 and mark2>50 and mark3>50 and mark4>50 and mark5>50) and (mark1<=75 and mark2<=75 and mark3<=75 and mark4<=75 and mark5<=75):
#     print("grade is 'B'")
# elif (mark1>75 and mark2>75 and mark3>75 and mark4>75 and mark5>75) and (mark1<=100 and mark2<=100 and mark3<=100 and mark4<=100 and mark5<=100):
#     print("grade is 'A'")
# elif (mark1>100 and mark2>100 and mark3>100 and mark4>100 and mark5>100):
#     print("invalid marks")
# else:
#     print("fail")

#find vowel or consonant
# character=str(input("enter the charcter: "))
# if character in ["a","e","i","o","u"]:
#     print(f"{character} it is a vowel")
# elif character not in ["a","e","i","o","u"]:
#     print(f"{character} it is a consonant")

# #calculate sales commission
# sales=int(input("enter the salea amount: "))
# if (sales>=0) and (sales<=10000):
#     print(f"commission is 0% {sales*0.00}")
# elif (sales>10000) and (sales<=20000):
#     print(f"commission is 5% {sales*0.05}")
# elif (sales>20000) and (sales<=50000):
#     print(f"commission is 10% {sales*0.1}")
# elif (sales>50000) and (sales<=100000):
#     print(f"commission is 15% {sales*0.15}")
# elif sales>100000:
#     print(f"commission is 20% {(sales*0.20)+500}")

# #calculate gross pay
# basic_salary=int(input("enter the basic salary: "))
# if (basic_salary>=0) and (basic_salary<=10000):
#     print(f"basic_salary + HRA + DA = gross_pay({basic_salary+(basic_salary*0.20)+(basic_salary*0.80)})")
# elif (basic_salary>10000) and (basic_salary<=20000):
#     print(f"basic_salary + HRA + DA = gross_pay({basic_salary+(basic_salary*0.25)+(basic_salary*0.90)})")
# elif basic_salary>20000:
#     print(f"basic_salary + HRA + DA = gross_pay({basic_salary+(basic_salary*0.30)+(basic_salary*0.95)})")

# # calculate tax for purchasing
# purchase_amount=int(input("enter the purchase amount: "))
# if purchase_amount>=0 and purchase_amount<=10000:
#     print(f"purchase_amount_tax={(purchase_amount*0.0)}")
# elif purchase_amount>10000 and purchase_amount<=20000:
#     purchase_amount_20000=(purchase_amount-10000)
#     purchase_amount_10000=purchase_amount-purchase_amount_20000
#     print(f"purchase_amount_tax={(purchase_amount_10000*0.0)+purchase_amount_20000*0.10}")
# elif purchase_amount>20000: #30000
#     purchase_amount_50000=(purchase_amount-20000) #10000
#     purchase_amount_20000=(purchase_amount-purchase_amount)-10000 #10000
#     purchase_amount_10000=(purchase_amount-(purchase_amount_50000+purchase_amount_20000)) #10000
#     print(f"purchase_amount_tax={(purchase_amount_10000*0.0)+(purchase_amount_20000*0.10)+(purchase_amount_50000*0.20)}")
    
# # calculate electricity bill
# units=int(input("enter the units: "))
# if units>=0 and units<=199:     
#     print(f"electricity_bill={units*1.20}")
#     value=units*1.20
# elif units>199 and units<=400:
#     units_200=(units-199)
#     units_199=units-units_200
#     print(f"electricity_bill={(units_199*1.20)+(units_200*1.50)}")
#     value=(units_199*1.20)+(units_200*1.50)
# elif units>400 and units<=600:
#     units_500=(units-400)
#     units_200=(units-units_500)-100
#     units_100=units-(units_500+units_200)
#     print(f"electricity_bill={(units_100*1.20)+(units_200*1.50)+(units_500*1.80)}")
#     value=(units_100*1.20)+(units_200*1.50)+(units_500*1.80)
# elif units>600:
#     units_1000=(units-600)
#     units_600=(units-units_1000)
#     units_500=(units_600-200)
#     units_200=(units_600-units_500)-100
#     units_100=units-(units_1000+units_500+units_200)
#     print(f"electricity_bill={(units_100*1.20)+(units_200*1.50)+(units_500*1.80)+(units_1000*2.00)}")
#     value=(units_100*1.20)+(units_200*1.50)+(units_500*1.80)+(units_1000*2.00)

# # If bill exceed Rs.400 then a surcharge of 15% will be charged and minimum bill should be Rs.100
# if value>400:
#     surcharge=value*0.15
#     value=value+surcharge
# if value<100:
#     value=100
# print(f"final electricity bill={value}")