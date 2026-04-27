# # print natural numbers till n
# n=10
# i=1
# while (i<=n):
#     print(i)
#     i=i+1

# # print even number till n
# n=10
# i=1
# while (i<=n):
#     if i%2==0:
#         print(i)
#     i=i+1

# #print odd number till n
# n=10
# i=1
# while (i<=n):
#     if i%2!=0:
#         print(i)
#     i=i+1

# # print numbers from -1 to -10
# n=-10
# i=-1
# while (i>=n):
#     print(i)
#     i=i-1
    
# # print numbers from -10 to -1
# n=-1
# i=-10
# while (i<=n):
#     print(i)
#     i=i+1

# #print natural numbers in reverse
# n=10
# i=1
# while(n>=i):
#     print(n)
#     n=n-1

# # print even numbers in reverse
# n=10
# i=1
# while(n>=i):
#     if n%2==0:
#         print(n)
#     n=n-1
    
# # print odd numbers in reverse
# n=10
# i=1
# while(n>=i):
#     if n%2!=0:
#         print(n)
#     n=n-1

# # print sum of natural numbers tiil n
# n=10
# i=1
# count=0
# while (i<=n):
#     count=count+i
#     # print(i)
#     i=i+1
# print(count)

# # print sum of even numbers tiil n
# n=10
# i=1
# count=0
# while (i<=n):
#     if i%2==0:
#         count=count+i
#         print(i)
#     i=i+1
# print(count)

# # print sum of odd numbers tiil n
# n=10
# i=1
# count=0
# while (i<=n):
#     if i%2!=0:
#         count=count+i
#         print(i)
#     i=i+1
# print(count)

# #1^2+2^2+3^2+....n^2 sum of naturals numbers
# n=10
# i=1
# count=0
# while (i<=n):
#     count=count+(pow(i,2))
#     # print(i)
#     i=i+1
# print(count)

# #1^2+3^2+5^2+....n^2 sum of odd numbers
# n=10
# i=1
# count=0
# while (i<=n):
#     if i%2!=0:
#         count=count+(pow(i,2))
#         # print(i)
#     i=i+1
# print(count)

# #2^2+4^2+6^2+....n^2 sum of odd numbers
# n=10
# i=1
# count=0
# while (i<=n):
#     if i%2==0:
#         count=count+(pow(i,2))
#         # print(i)
#     i=i+1
# print(count)

# # print sum of cube numbers till n
# n=10
# i=1
# count=0
# while (i<=n):
#     count=count+(pow(i,3))
#     print(i)
#     i=i+1
# print(count)

# # 1/1^2+1/2^2+1/3^2+....1/n^2 sum of natural numbers 
# n=10
# i=1
# count=0
# while (i<=n):
#     count=count+(1/(pow(i,2)))
#     print(i)
#     i=i+1
# print(count)

# # 1/1^2+1/3^2+1/5^2+....1/n^2 sum of odd numbers 
# n=10
# i=1
# count=0
# while (i<=n):
#     if i%2!=0:
#         count=count+(1/(pow(i,2)))
#         print(i)
#     i=i+1
# print(count)

# # 1/2^2+1/4^2+1/6^2+....1/n^2 sum of even numbers 
# n=10
# i=1
# count=0
# while (i<=n):
#     if i%2==0:
#         count=count+(1/(pow(i,2)))
#         print(i)
#     i=i+1
# print(count)

# # find factorial value for n
# import math
# n=10
# i=1
# while (i<=n):
    # factorial=math.factorial(n)
#    # print(i)
#    # print(math.factorial)
#     i=i+1
# print(factorial)   

# # 1! + 2! + 3! +……+n! for natural numbers
# import math
# n=10
# i=1
# count=0
# while (i<=n):
#     count=count+(math.factorial(i))
#     # print(i)
#     i=i+1
# print(count)

# # 1! + 3! + 5! +……+n! for odd numbers
# import math
# n=10
# i=1
# count=0
# while (i<=n):
#     if i%2!=0:
#         count=count+(math.factorial(i))
#         # print(i)
#     i=i+1
# print(count)

# # 2! + 4! + 6! +……+n! for even numbers
# import math
# n=10
# i=1
# count=0
# while (i<=n):
#     if i%2==0:
#         count=count+(math.factorial(i))
#         # print(i)
#     i=i+1
# print(count)

# # 1/1! + 1/2! + 1/3! +……+1/n! for natural numbers
# import math
# n=10
# i=1
# count=0
# while (i<=n):
#     count=count+(1/(math.factorial(i)))
#     # print(i)
#     i=i+1
# print(count)

# # 1/1! + 1/3! + 1/5! +……+1/n! for odd numbers
# import math
# n=10
# i=1
# count=0
# while (i<=n):
#     if i%2!=0:
#         count=count+(1/(math.factorial(i)))
#         # print(i)
#     i=i+1
# print(count)

# # 1/2! + 1/4! + 1/6! +……+1/n! for even numbers
# import math
# n=10
# i=1
# count=0
# while (i<=n):
#     if i%2==0:
#         count=count+(1/(math.factorial(i)))
#         # print(i)
#     i=i+1
# print(count)

# # Print current and previous Odd number till n
# n=10
# i=1
# while (n>=i):
#     if n%2!=0:
#         # print(n)
#         print(f"current no: {n}")
#         print(f"previous no: {n-2}")
#     n=n-1

# # Print current and previous even number till n
# n=10
# i=1
# while (n>=i):
#     if n%2==0:
#         # print(n)
#         print(f"current no: {n}")
#         print(f"previous no: {n-2}")
#     n=n-1

# #  N Multiplication table till m
# m=10
# i=1
# n=5
# while (i<=m):
#     print(f"{i}*{n}={i*n}")
#     i=i+1

# # Reverse s number
# n=1234
# reverse=0
# while(n>0):
#     last_digit=n%10
#     reverse=reverse*10+last_digit
#     n//=10
#     # print(n)
#     # n=n+1
# print(reverse)

# # Print each character in string
# n="jaga"
# len_n=len(n)-1
# i=0
# while (i<=len_n):
#     print(n[i])
#     i=i+1
    
# # Reverse a string
# n="jaga"
# len_n=len(n)-1
# i=0
# reverse=[]
# while (len_n>=i):
#     print(n[len_n],len_n)
#     reverse.append(n[len_n])
#     len_n=len_n-1
# print("".join(reverse))

# # Check whether giver number is palindrome or not
# n=121
# n1=n
# reverse=0
# while(n>0):
#     last_digit=n%10
#     reverse=reverse*10+last_digit
#     n//=10
# print(reverse)
# if reverse==n1:
#     print("Palindrome")
# else:
#     print("Not palindrome")

# # Check whether giver number is Armstrong or not
# n=153
# n1=n
# order=len(str(n))
# sum=0       
# while(n>0):
#     last_digit=n%10
#     sum=sum+pow(last_digit,order)
#     n//=10
# print(sum)
# if sum==n1:
#     print("Armstrong")
# else:
#     print("Not Armstrong")  
    
# # Check whether given number is Adam or not
# n=12
# n1=n
# reverse=0       
# while(n>0):
#     last_digit=n%10
#     reverse=reverse*10+last_digit
#     n//=10  
# print(reverse)
# reverse2=reverse*reverse
# print(reverse2)
# reverse=0
# while (reverse2>0):
#     last_digit=reverse2%10
#     reverse=reverse*10+last_digit
#     reverse2//=10
# print(reverse)
# print(n1)
# if reverse==n1*n1:
#     print("Adam")
# else:    
#     print("Not Adam")

# # Check whether given number is Perfect number or Not
# n=28
# sum=0
# i=1
# while (i<n):
#     if n%i==0:
#         sum=sum+i
#     i=i+1
# if sum==n:
#     print("Perfect number")
# else:
#     print("Not Perfect number")

#### decimal
# # Convert given number from decimal to binary
# decimal=45
# binary=[]
# while(decimal>0):
#     binary.append(decimal%2)
#     decimal=decimal//2
# print(binary)

# # Convert given number from decimal to octal
# decimal=45
# octal=[]
# while(decimal>0):
#     octal.append(decimal%8)
#     decimal=decimal//8
# print(octal)

# # Convert given number from decimal to hexadecimal.
# decimal=45
# hexadecimal=[]
# while(decimal>0):
#     hexadecimal.append(decimal%16)
#     decimal=decimal//16
# # print(hexadecimal)
# i=0
# while (i<=(len(hexadecimal)-1)):
#     if hexadecimal[i]==10:
#         hexadecimal[i]="a"
#     elif hexadecimal[i]==11:
#         hexadecimal[i]="b"
#     elif hexadecimal[i]==12:
#         hexadecimal[i]="c"
#     elif hexadecimal[i]==13:
#         hexadecimal[i]="d"
#     elif hexadecimal[i]==14:
#         hexadecimal[i]="e"
#     elif hexadecimal[i]==15:
#         hexadecimal[i]="f"
#     print(hexadecimal[i])
#     i=i+1
# print(hexadecimal)

#### binary
# # Convert given number from binary to decimal.
# binary=1101
# decimal=0
# i=0
# while (1<=binary):
#     last_digit=(binary%10)
#     # print(last_digit,i)
#     decimal=decimal+(last_digit*(pow(2,i)))
#     binary=binary//10
#     i=i+1
# print(decimal)

# # Convert given number from binary to octal.
# binary=101101
# octal=[]
# i=0
# while (binary>0):
#     last_digit=(binary%1000)
#     octal.append(last_digit)
#     binary=binary//1000
#     i=i+1
# # print(octal)
# i=0
# while (i<=(len(octal)-1)):
#     # print(octal[i])
#     if octal[i]==000:
#         octal[i]=0
#     elif octal[i]==0o01:
#         octal[i]=1  
#     elif octal[i]==0o10:
#         octal[i]=2
#     elif octal[i]==0o11:
#         octal[i]=3
#     elif octal[i]==100:
#         octal[i]=4
#     elif octal[i]==101:
#         octal[i]=5
#     elif octal[i]==110:
#         octal[i]=6
#     elif octal[i]==111:
#         octal[i]=7
#     # print(octal[i])
#     i=i+1
# print("".join(map(str,octal)))

# # Convert given number from binary to hexadecimal.
# binary=00101101
# len_binary=len(str(binary))-1
# hexadecimal=[]
# i=0
# while (i<=len_binary):
#     print(i,binary)
#     i=i+1

#### octal

#### hexadecimal




# # Check whether given number is Prime number or Not.
# n=29
# len_n=1
# # print(len_n)
# i=1
# while (i<=len_n):
#     if n==1 or n==2 or n==3:
#         print(f"{n} is prime number")
#     elif n%i==0 and n%n==0 and n%2!=0 and n%3!=0:
#         print(f"{n} is prime number")
#     else:
#         print(f"{n} is not prime number")
#     i=i+1

# # Fibonacci series.(0,1,1,2,3,5,8,13…..n)
# n=10 #0,1,1,2,3,5,8,13,21,34,55,89,144
# i=0
# a,b=0,1
# sequence=[]
# while(i<=n):
#     sequence.append(a)
#     a,b=b,a+b
#     i=i+1
# print(sequence)

# # Pell series .p2=p0+2p1, p0=0, p1=1. (0, 1, 2, 5, 12, 29….n).
# n=10
# i=0
# a,b=0,1
# sequence=[]
# while(i<=n):
#     # print(i)
#     sequence.append(a)
#     a,b=b,b*2+a
#     i=i+1
# print(sequence)

# # Convert time, 
# # i. Hour to sec. 
# hour=2
# seconds=3600
# i=1
# while (i<=hour):
#     seconds=hour*seconds
#     i=hour+1
# print(seconds)

# # ii. Min to hour.    
# minutes=150
# hour=60
# i=1
# while (i<=minutes):
#     hour=minutes/hour
#     i=minutes+1
# print(hour)

# # iii. Sec to min.
# seconds=180
# minutes=60
# i=0
# while(i<=seconds):
#     minutes=seconds/60
#     i=seconds+1
# print(minutes)

# # Count number of digits of a number.
# numbers=12445
# # len_numbers=len(str(numbers))
# # print(len_numbers)
# i=1
# count=0
# while (i<=numbers):
#     last=numbers%10
#     count=count+1
#     numbers//=10
# print(count)

# # Calculate sum of digits of a number
# numbers=12445
# # len_numbers=len(str(numbers))
# # print(len_numbers)
# i=1
# count=0
# while (i<=numbers):
#     last=numbers%10
#     count=count+last
#     numbers//=10
# print(count)

# # Calculate product of digits of a number.
# numbers=12445
# # len_numbers=len(str(numbers))
# # print(len_numbers)
# i=1
# count=1
# while (i<=numbers):
#     last=numbers%10
#     count=count*last
#     numbers//=10
# print(count)

# # Swapping first and last digit of a number.
# numbers=1234
# i=1
# while (i<=numbers):
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
# i=1
# inputs=[]
# while(i<=n):
#     inputs=int(input("enter: "))
#     if inputs>0:
#         print(f"{inputs} is positive")
#     elif inputs<0:
#         print(f"{inputs} is negative")
#     else:
#         print(f"{inputs} is zero")
#     i=i+1
# print(inputs)

# # Find biggest number for n time’s value.
# n=5
# i=1
# inputss=[]
# while(i<=n):
#     inputs=int(input("enter: "))
#     inputss.append(inputs)
#     i=i+1
# # print(f"biggest number is: {max(inputss)}")
# print(inputss)
# i=0
# biggest=inputss[0]
# while (i<=len(inputss)-1):
#     if biggest<inputss[i]:
#         biggest=inputss[i]
#     i=i+1
# print(f"biggest number is: {biggest}")

# # Find smallest number for n time’s value.
# n=5
# i=1
# inputss=[]
# while (i<=n):
#     inputs=int(input("enter: "))
#     inputss.append(inputs)
#     i=i+1
# print(inputss)
# i=0
# smallest=inputss[0]
# while (i<=len(inputss)-1):
#     print(i)
#     if smallest>inputss[i]:
#         smallest=inputss[i]
#     i=i+1
# print(f"biggest number is: {smallest}")

# # Sum of numbers for n times value
# n=5
# i=1
# inputss=[]
# while (i<=n):
#     inputs=int(input("enter: "))
#     inputss.append(inputs)
#     i=i+1
# # print(f"sum of number is: {sum(inputss)}")
# print(inputss)
# i=0
# count=0
# while (i<=len(inputss)-1):
#     count=count+inputss[i]
#     i=i+1
# print(f"sum of number is: {count}")

# # Sum of odd number for n times value
# n=5
# i=1
# inputss=[]
# while (i<=n):
#     inputs=int(input("enter: "))
#     inputss.append(inputs)
#     i=i+1
# print(inputss)
# i=0
# count=0
# while (i<=len(inputss)-1):
#     if inputss[i]%2!=0:
#         count=count+inputss[i]
#     i=i+1
# print(f"sum of odd number is: {count}")

# # Sum of even number for n times value.
# n=5
# i=1
# inputss=[]
# while (i<=n):
#     inputs=int(input("enter: "))
#     inputss.append(inputs)
#     i=i+1
# print(inputss)
# i=0
# count=0
# while (i<=len(inputss)-1):
#     if inputss[i]%2==0:
#         count=count+inputss[i]
#     i=i+1
# print(f"sum of even number is: {count}")

# # Find sum and average n time’s number
# n=5
# i=1
# inputss=[]
# while (i<=n):
#     inputs=int(input("enter: "))
#     inputss.append(inputs)
#     i=i+1
# # print(f"sum of number is: {sum(inputss)}")
# print(inputss)
# i=0
# sum=0
# while (i<=len(inputss)-1):
#     sum=sum+inputss[i]
#     i=i+1
# print(f"sum of number is: {sum}")
# print(f"average of number is: {sum/n}")

# # Find highest common factor (HCF) for 2 numbers.
# n=int(input("enter: "))
# m=int(input("enter: "))
# i=1
# hcf=1
# while (i<=n and i<=m):
#     if n%i==0 and m%i==0:
#         # print(i)
#         hcf=i
#     i=i+1
# print(f"HCF is: {hcf}")

# # Find least common multiple (LCM) for 2 numbers.
# n=int(input("enter: "))
# m=int(input("enter: "))
# i=1
# hcf=1
# while (i<=n and i<=m):
#     if n%i==0 and m%i==0:
#         # print(i)
#         hcf=i
#     i=i+1
# # print(f"HCF is: {hcf}")
# lcm=(n*m)/hcf
# print(f"LCM is: {lcm}")

# # Check whether given number is prime Adam or not.
# n=31
# len_n=1
# # print(len_n)
# i=1
# is_prime=True
# while (i<=len_n):
#     if n==1 or n==2 or n==3:
#         # print(f"{n} is prime number")
#         is_prime=True
#         # n=n
#     elif n%i==0 and n%n==0 and n%2!=0 and n%3!=0:
#         # print(f"{n} is prime number")
#         is_prime=True
#         # n=n
#     else:
#         # print(f"{n} is not prime number")
#         is_prime=False
#         # n=0
#     i=i+1
# print(is_prime)
# # print(n)
# n1=n
# # print(n1)
# reverse=0
# if is_prime:      
#     while(n>0):
#         last_digit=n%10
#         reverse=reverse*10+last_digit
#         n//=10  
#     # print(reverse)
#     reverse2=reverse*reverse
#     # print(reverse2)
#     reverse=0
#     while (reverse2>0):
#         last_digit=reverse2%10
#         reverse=reverse*10+last_digit
#         reverse2//=10
#     # print(reverse)
#     # print(n1)
#     if reverse==n1*n1 and (reverse and n1)>0:
#         print("prime adam")
#     else:    
#         print("Not prime adam")

# # Check whether given number Automorphic or not
# n=25
# square=pow(n,2)
# # print(square)
# i=1
# while (i<=n):
#     last_digit=square%10
#     if last_digit==n%10:
#         print("Automorphic")
#         break
#     else:
#         print("Not Automorphic")
#         break
#     i=i+1

# # Enter a=0, b=0, c=0 and get n value to print the following pattern.
# a=0
# b=0
# c=0
# n=1
# i=0
# while (i<=n*111):
#     print(a,b,c)
#     c=c+1
#     if(c==10):
#         c=0
#         b=b+1
#     if(b==10):
#         b=0
#         a=a+1
#     i=i+1
