# #find equivalent day for given number
# day=int(input("enter the day no: "))
# match day:
#     case 1:
#         print("it is sunday")
#     case 2:
#         print("it is monday")
#     case 3:
#         print("it is tuesday")  
#     case 4:
#         print("it is wednesday")
#     case 5:
#         print("it is thursday")
#     case 6:
#         print("it is friday")
#     case 7:
#         print("it is saturday")
#     case _:
#         print("invalid day")

# #find equivalent month for given number
# month=int(input("enter the month no: "))
# match month:
#     case 1:
#         print("it is jan")
#     case 2:
#         print("it is feb")
#     case 3:
#         print("it is mar")  
#     case 4:
#         print("it is apr")
#     case 5:
#         print("it is may")
#     case 6:
#         print("it is jun")
#     case 7:
#         print("it is jul")
#     case 8:
#         print("it is ags")
#     case 9:
#         print("it is sep")
#     case 10:
#         print("it is oct")
#     case 11:
#         print("it is nov")
#     case 12:
#         print("it is dec")
#     case _:
#         print("invalid month")

# # to find the no of days in month
# month=int(input("enter the month no: "))
# match month:
#     case 1|3|5|7|8|10|12:
#         print(f"{month} has 31 days")
#     case 4|6|9|11:
#         print(f"{month} has 30 days")
#     case 2:
#         print(f"{month} has 28 days")
#     case _:
#         print("invalid month")

# # check wheather an alphabet is vowel or consonant
# alpha=input("enter an alphabet: ")
# match alpha:
#     case 'a'|'e'|'i'|'o'|'u'|'A'|'E'|'I'|'O'|'U':
#         print(f"{alpha} is vowel")
#     case _:
#         print(f"{alpha} is consonant")

# # write a program to calculate function (add, sub, mul, div, mod) using switch case
# a=int(input("enter a value: "))
# b=int(input("enter a value: "))     
# op=input("enter the operator: ")
# match op:
#     case '+':
#         c=a+b
#         print("sum:",c)
#     case '-':
#         c=a-b
#         print("sub:",c)
#     case '*':
#         c=a*b
#         print("mul:",c)
#     case '/':
#         c=a/b
#         print("div:",c)
#     case '%':
#         c=a//b
#         print("mod:",c)
#     case _:
#         print("invalid operator")

# # write a program to print entered no in word using switch case
# num=int(input("enter a number: "))
# match num:
#     case 0:
#         print("zero")
#     case 1:
#         print("one")
#     case 2:
#         print("two")
#     case 3:
#         print("three")
#     case 4:
#         print("four")
#     case 5:
#         print("five")
#     case 6:
#         print("six")
#     case 7:
#         print("seven")
#     case 8:
#         print("eight")
#     case 9:
#         print("nine")
#     case _:
#         print("invalid number")

# # Write a program to input sum, rate, time and type of Interest 
# # ('S' for Simple Interest and 'C'for Compound Interest). 
# # Calculate and display the sum and the interest earned.
# interest=str(input(" enter si or ci"))
# match(interest):
#     case "SI"|"si":
#         p=int(input("enter p: "))
#         r=int(input("enter r: "))
#         t=int(input("enter t: "))
#         print(f"Simple Interest: {(p * r * t) / 100}")
#     case "CI"|"ci":
#         p=int(input("enter p: "))
#         r=int(input("enter r: "))
#         t=int(input("enter t: "))
#         print(f"Simple Interest: {p *((1 + (r / 100))* t - 1)}")
#     case _:
#         print("invalid")
        
# # Write a program to calculate Celsius, Fahrenheit, Kelvin
# temp=str(input("enter: "))
# match(temp):
#     case "Fahrenheit to Celsius"|"f to c"|"F To C":
#         f=int(input("enter f: "))
#         print(f"c: {(f-32)*5/9}")
#     case "Celsius to Fahrenheit"|"c to f"|"C to F":
#         c=int(input("enter c: "))
#         print(f"f: {(c*5/9+32)}")
#     case "Celsius to kelvin"|"c to k"|"C to K":
#         c=int(input("enter c: "))
#         print(f"k: {c+273.15}")
#     case "Kelvin to Celsius"|"k to c"|"K to C":
#         k=int(input("enter c: "))
#         print(f"c: {k-273.15}")
#     case "Kelvin to Fahrenheit"|"k to f"|"K to F":
#         k=int(input("enter c: "))
#         print(f"f: {(k-273.15)*9/5+32}")
#     case "Fahrenheit to kelvin"|"f to k"|"F to K":
#         f=int(input("enter c: "))
#         print(f"k: {(f-32)*5/9-273.15}")
#     case _:
#         print("invalid")
