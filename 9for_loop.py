# # Print Natural number till n.
# n=10
# for i in range(n):
#     print(i+1)
    
# # Print Even number till n.
# n=10
# for i in range(n+1):
#     if i%2==0:
#         print(i)

# # Print Odd number till n.
# n=10
# for i in range(n+1):
#     if i%2!=0:
#         print(i)

# # Print number from -10 to -1.
# n=-10
# for i in range(n,0):
#     print(i)

# # Print natural number in reverse.
# n=10
# for i in range(n,0,-1):
#     print(i)

# # Print Even number in reverse.
# n=10
# for i in range(n,0,-1):
#     if i%2==0:
#         print(i)
        
# # Print odd number in reverse.
# n=10
# for i in range(n,0,-1):
#     if i%2!=0:
#         print(i)

# # Print Sum of natural number till n
# n=10
# count=0
# for i in range(1,n+1):
#     count=count+i
#     # print(i)
# print(count)

# # Print sum of odd number till n.
# n=10
# count=0
# for i in range(1,n+1):
#     if i%2!=0:
#         count=count+i
#         # print(i)
# print(count)

# # Print sum of even number till n.
# n=10
# count=0
# for i in range(1,n+1):
#     if i%2==0:
#         count=count+i
#         # print(i)
# print(count)

# # 1^2+2^2+3^2+….+n^2
# n=10
# count=0
# for i in range(1,n+1):
#     count=count+i**2
#     # print(i)
# print(count)

# # 1^2+3^2+5^2+….+n^2
# n=10
# count=0
# for i in range(1,n+1):
#     if i%2!=0:
#         count=count+i**2
#         # print(i)
# print(count)

# # 2^2+4^2+6^2+….+n^2
# n=10
# count=0
# for i in range(1,n+1):
#     if i%2==0:
#         count=count+i**2
#         # print(i)
# print(count)

# # Print sum of cube number till n.
# n=10
# count=0
# for i in range(1,n+1):
#     count=count+pow(i,3)
#     # print(i)
# print(count)

# # 1/1^2+1/2^2+1/3^2+….+1/n^2
# n=10
# count=0
# for i in range(1,n+1):
#     count=count+(1/pow(i,2))
#     # print(i)
# print(count)

# # 1/1^2+1/3^2+1/5^2+….+1/n^2
# n=10
# count=0
# for i in range(1,n+1):
#     if i%2!=0:
#         count=count+(1/pow(i,2))
#         # print(i)
# print(count)

# # 1/2^2+1/4^2+1/6^2+….+1/n^2
# n=10
# count=0
# for i in range(1,n+1):
#     if i%2==0:
#         count=count+(1/pow(i,2))
#         # print(i)
# print(count)

# # Find Factorial value for n.
# n=10
# count=1
# for i in range(1,n+1):
#     count=count*i
#     # print(i)
# print(count)

# # 1! + 2! + 3! +……+n!
# import math
# n=10
# count=0
# for i in range(1,n+1):
#     count=count+(math.factorial(i))
#     # print(i)
# print(count)

# # 1! + 3! + 5! +……+n!
# import math
# n=10
# count=0
# for i in range(1,n+1):
#     if i%2!=0:
#         count=count+(math.factorial(i))
#         # print(i)
# print(count)

# # 2! + 4! + 6! +……+n!
# import math
# n=10
# count=0
# for i in range(1,n+1):
#     if i%2==0:
#         count=count+(math.factorial(i))
#         # print(i)
# print(count)

# # 1/1! + 1/2! + 1/3! +……+1/n!
# import math
# n=10
# count=0
# for i in range(1,n+1):
#     count=count+(1/math.factorial(i))
#     # print(i)
# print(count)

# # 1/1! + 1/3! + 1/5! +……+1/n!
# import math
# n=10
# count=0
# for i in range(1,n+1):
#     if i%2!=0:
#         count=count+(1/math.factorial(i))
#         # print(i)
# print(count)

# # 1/2! + 1/4! + 1/6! +……+1/n!
# import math
# n=10
# count=0
# for i in range(1,n+1):
#     if i%2==0:
#         count=count+(1/math.factorial(i))
#         # print(i)
# print(count)

# # Print current and previous Odd number till n.
# n=10
# for i in range(1,n+1):
#     if i%2!=0:
#         print("current odd number: ",i)
#         print("previous odd number: ",i+2)
#         # print(i)
        
# # Print current and previous even number till n.
# n=10
# for i in range(1,n+1):
#     if i%2==0:
#         print("current even number: ",i)
#         print("previous even number: ",i+2)
#         # print(i)

# # Nth Multiplication table till m.
# n=10
# m=5
# for i in range (1,n+1):
#     print(f"{i}*{m}= {i*m}")
#     # print(i)

# # Reverse s number.
# n=12345
# reverse=0
# for i in str(n):
#     last_digit=n%10
#     reverse=reverse*10+last_digit
#     n//=10
#     # print(i)
# print(reverse)

# # Print each character in string.
# n="jaga"
# for i in n:
#     print(i)
    
# # Reverse a string.
# n="jaga"
# len_n=len(n)-1
# # print(len_n)
# reverse=[]
# for i in range(len_n,-1,-1):
#     reverse.append(n[i])
#     print(i,n[i])
# print("".join(reverse))

# # Check whether giver number is palindrome or not.
# n=102
# n1=n
# reverse=0
# for i in str(n):
#     last_digit=n%10
#     reverse=reverse*10+last_digit
#     n//=10
# if n1==reverse:
#     print(f"{n1} is palindrome")
# else:
#     print(f"{n1} is not palindrome")
# # print(n1,reverse)

# # Check whether giver number is Armstrong or not.
# n=153
# n1=n
# len_n=len(str(n))
# # print(len_n)
# sum=0
# for i in str(n):
#     last_digit=n%10
#     sum=sum+pow(last_digit,len_n)
#     n//=10
# # print(sum)
# if sum==n1:
#     print("Armstrong")
# else:
#     print("Not Armstrong")  

# # Check whether given number is Adam or not.
# n=12
# n1=n
# square_n=pow(n,2)
# square_reverse_n=0
# for i in str(square_n):
#     last_digit=square_n%10
#     square_reverse_n=square_reverse_n*10+last_digit
#     square_n//=10
#     # print(i)
# # print(square_reverse_n)
# reverse_n=0
# for i in str(n1):
#     last_digit=n1%10
#     reverse_n=reverse_n*10+last_digit
#     n1//=10
#     # print(i)
# # print(reverse_n)
# reverse_square_n=pow(reverse_n,2)
# # print(reverse_square_n)
# if reverse_square_n==square_reverse_n:
#     print("it is adam number")
# else:
#     print("it is not a adam number")

# # Check whether given number is Perfect number or Not.
# n=28
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         print(i)
#         sum=sum+i
#     i=i+1
# if sum==n:
#     print("Perfect number")
# else:
#     print("Not Perfect number")






# # Check whether given number is Prime number or Not.
# n=28
# n1=n
# # print(len_n)
# prime=True
# for i in range(1,n+1):
#     if n==1 or n==2 or n==3:
#         # print(f"{n} is prime number")
#             prime=True
#             break
#     elif n%i==0 and n%n==0 and n%2!=0 and n%3!=0:
#         # print(f"{n} is prime number")
#         prime=True
#         break
#     else:
#         # print(f"{n} is not prime number")
#         prime=False
#     # print(n,i)
# if prime:
#     print(f"{n} is prime number")
# else:
#     print(f"{n} is not prime number")
    
# # Fibonacci series.(0,1,1,2,3,5,8,13…..n)
# n=10 #0,1,1,2,3,5,8,13,21,34,55,89,144
# a,b=0,1
# sequence=[]
# for i in range(0,n+1):
#     sequence.append(a)
#     a,b=b,a+b
# print(sequence)

# # Pell series .p2=p0+2p1, p0=0, p1=1. (0, 1, 2, 5, 12, 29….n).
# n=10
# a,b=0,1
# sequence=[]
# for i in range(0,n+1):
#     # print(i)
#     sequence.append(a)
#     a,b=b,b*2+a
# print(sequence)

# # Convert time,
# # i. Hour to sec.
# hour=22
# sec=3600
# for i in str(1):
#     sec=hour*sec
#     print(hour)
# print(sec)

# # ii. Min to hour
# min=150
# hour=60
# for i in str(1):
#     hour=min/hour
#     # print(min)
# print(hour)

# # iii. Sec to min.
# sec=180
# min=60
# for i in str(1):
#     min=sec/min
#     # print(sec)
# print(min)

# # Count number of digits of a number.
# n=12345
# # len_n=len(str(n))
# # print(len_n)
# count=0
# for i in str(n):
#     count=count+1
#     # print(i)
# print(count)

# # Calculate sum of digits of a number.
# n=12345
# # len_n=len(str(n))
# # print(len_n)
# count=0
# for i in str(n):
#     count=count+int(i)
#     # print(i)
# print(count)

# # Calculate product of digits of a number.
# numbers=12445
# # len_numbers=len(str(numbers))
# # print(len_numbers)
# count=1
# for i in str(numbers):
#     print(i)
#     count=count*int(i)
# print(count)

# # Swapping first and last digit of a number.
# numbers=1234
# i=1
# for i in str(1):
#     last_digit=(numbers%10)*1000
#     first_digit=(numbers//1000)*1
#     second_digit=(numbers%1000)//100*100
#     third_digit=(numbers%100)//10*10
#     if first_digit and last_digit:
#         last_digit=last_digit+first_digit
#         first_digit=last_digit-first_digit
#         last_digit=last_digit-first_digit
#     i=numbers+1
# print(first_digit+second_digit+third_digit+last_digit)

# # Find positive, negative, and zero for nth value.
# n=5
# # i=1
# inputs=[]
# for i in range(1,n+1):
#     inputs=int(input("enter: "))
#     if inputs>0:
#         print(f"{inputs} is positive")
#     elif inputs<0:
#         print(f"{inputs} is negative")
#     else:
#         print(f"{inputs} is zero")
# print(inputs)

# # Find biggest number for n time’s value.
# n=5
# inputss=[]
# for i in range(1,n+1):
#     inputs=int(input("enter: "))
#     inputss.append(inputs)
# # print(f"biggest number is: {max(inputss)}")
# print(inputss)
# biggest=inputss[0]
# for i in range(1,len(inputss)):
#     if biggest<inputss[i]:
#         biggest=inputss[i]
# print(f"biggest number is: {biggest}")

# # Find smallest number for n time’s value.
# n=5
# inputss=[]
# for i in range(1,n+1):
#     inputs=int(input("enter: "))
#     inputss.append(inputs)
# # print(f"biggest number is: {max(inputss)}")
# print(inputss)
# biggest=inputss[0]
# for i in range(1,len(inputss)):
#     if biggest>inputss[i]:
#         biggest=inputss[i]
# print(f"smallest number is: {biggest}")

# # Sum of numbers for n times value.
# n=5
# inputss=[]
# # while (i<=n):
# for i in range(1,n+1):
#     inputs=int(input("enter: "))
#     inputss.append(inputs)
# # print(f"sum of number is: {sum(inputss)}")
# print(inputss)
# count=0
# for i in range(0,len(inputss)):
#     count=count+inputss[i]
# print(f"sum of number is: {count}")

# # Sum of odd number for n times value.
# n=5
# inputss=[]
# # while (i<=n):
# for i in range(1,n+1):
#     inputs=int(input("enter: "))
#     inputss.append(inputs)
# # print(f"sum of number is: {sum(inputss)}")
# print(inputss)
# count=0
# for i in range(0,len(inputss)):
#     if inputss[i]%2!=0:
#         count=count+inputss[i]
# print(f"sum of number is: {count}")

# #  Sum of even number for n times value.
# n=5
# inputss=[]
# # while (i<=n):
# for i in range(1,n+1):
#     inputs=int(input("enter: "))
#     inputss.append(inputs)
# # print(f"sum of number is: {sum(inputss)}")
# print(inputss)
# count=0
# for i in range(0,len(inputss)):
#     if inputss[i]%2==0:
#         count=count+inputss[i]
# print(f"sum of number is: {count}")

# # Find sum and average n time’s number.
# n=5
# inputss=[]
# for i in range(1,n+1):
#     inputs=int(input("enter: "))
#     inputss.append(inputs)
#     i=i+1
# # print(f"sum of number is: {sum(inputss)}")
# print(inputss)
# sum=0
# for i in range(0,len(inputss)):
#     sum=sum+inputss[i]
#     i=i+1
# print(f"sum of number is: {sum}")
# print(f"average of number is: {sum/n}")

# # Find highest common factor (HCF) for 2 numbers.
# n=int(input("enter: "))
# m=int(input("enter: "))
# hcf=1
# for i in range(1,n+1):
#     # print(i)
#     if n%i==0 and m%i==0:
#         # print(i)
#         hcf=i
# print(f"HCF is: {hcf}")

# # Find least common multiple (LCM) for 2 numbers.
# n=int(input("enter: "))
# m=int(input("enter: "))
# hcf=1
# for i in range(1,n+1):
#     if n%i==0 and m%i==0:
#         # print(i)
#         hcf=i
#     i=i+1
# # print(f"HCF is: {hcf}")
# lcm=(n*m)/hcf
# print(f"LCM is: {lcm}")

# # Check whether given number is prime Adam or not.
# n=31
# is_prime=True
# for i in range(1,n+1):
#     if n==1 or n==2 or n==3:
#         is_prime=True
#     elif n%i==0 and n%n==0 and n%2!=0 and n%3!=0:
#         is_prime=True
#     else:
#         is_prime=False
# print(is_prime)
# n1=n
# reverse=0
# if is_prime:      
#     for i in str(n):
#         last_digit=n%10
#         reverse=reverse*10+last_digit
#         n//=10  
#     # print(reverse)
#     reverse2=reverse*reverse
#     # print(reverse2)
#     reverse=0
#     for i in str(reverse2):
#         last_digit=reverse2%10
#         reverse=reverse*10+last_digit
#         reverse2//=10
#     # print(reverse)
#     # print(n1)
#     if reverse==n1*n1 and (reverse and n1)>0:
#         print("prime adam")
#     else:    
#         print("Not prime adam")
# else:
#     print("Not prime adam")

# # Check whether given number Automorphic or not
# n=25
# square=pow(n,2)
# # print(square)
# for i in str(1):
#     last_digit=square%10
#     if last_digit==n%10:
#         print("Automorphic")
#         break
#     else:
#         print("Not Automorphic")
#         break

# # Enter a=0, b=0, c=0 and get n value to print the following pattern.
# a=0
# b=0
# c=0
# n=1
# for i in range(1,(n*111)+2):
#     print(a,b,c)
#     c=c+1
#     if(c==10):
#         c=0
#         b=b+1
#     if(b==10):
#         b=0
#         a=a+1
#     # print(i)
