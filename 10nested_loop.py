########################################## while loop
# #  Print palindrome numbers
# n=int(input("Enter n value="))
# i=1
# while(i<=n):
#     j=0
#     a=i
#     while(a>0):
#         mod=a%10
#         j=j*10+mod
#         a=a//10
#     if(j==i):
#         print("Palindrome",i)
#     i=i+1

# #  Print palindrome numbers from 100 to 999
# n=999
# i=100
# while (i<=n):
#     # print(i)
#     a=i
#     b=0
#     while (a>0):
#         last=a%10
#         b=b*10+last
#         a=a//10
#     if (i==b):
#         print("palindrome",i)
#     i=i+1
    
# # Print prime numbers from 1 to 100.
# n=100
# i=1
# while (i<=n):
#     a=i
#     b=0
#     while (a>0):
#         last=a
#         # b=b*10+last
#         if last==1 or last==2 or last==3 or last==5 or last==7:
#             b=last
#         elif last%i==0 and last%last==0 and last%2!=0 and last%3!=0 and last%5!=0 and last%7!=0:
#             b=last
#         a=a//100
#     if i==b:
#         print(i)
#     i=i+1

# # Print Armstrong numbers from 100 to n.
# n=200
# i=1
# while (i<=n):
#     a=i
#     b=0
#     # print(i)
#     len_n=len(str(i))
#     while (a>0):
#         last_digit=a%10
#         b=b+pow(last_digit,len_n)
#         a=a//10
#     if b==i:
#         print("armstrong",i)
#     i=i+1

# # Print Adam numbers from 100 to n.
# n=100
# i=1
# while (i<=n):
#     a=i #12
#     square_i=pow(i,2) #12>>144
#     b1=0
#     while (square_i>0):
#         last1=square_i%10
#         b1=b1*10+last1 #441
#         square_i=square_i//10
#     # print("square_reverse",b1)
#     b=0
#     while (a>0):
#         last=a%10
#         b=b*10+last #12>>21
#         a=a//10
#     # print("reverse",b)
#     # print(a)
#     if b1==pow(b,2):
#         print(i,"adam")
#     i=i+1

# # # Calculate student grade for each subject.
# no_of_students=3
# no_of_subjects=5
# i=1
# while i<=no_of_students:
#     enter=str(input("enter name: "))
#     a=1
#     total=0
#     while (a<=no_of_subjects):
#         subjects=int(input("enter marks: "))
#         total=total+subjects
#         a=a+1
#     print(enter)
#     print(total)
#     i=i+1

# # Find whether the given number is strong number.
# import math
# n=145
# i=1
# while(n>=i):
#     a=n
#     b=0
#     while (a>0):
#         last=a%10
#         b=b+math.factorial(last)
#         a=a//10
#     # print(n)
#     if b==n:
#         print(f"it is strong number {n}")
#     else:
#        print(f"it is not a strong number {n}") 
#     n=n-n

# # Multiplication table chart.
# n=10
# m=5
# i=1
# while (i<=n):
#     print(f"{i}*{m}= {i*m}")
#     # print(i)
#     i=i+1
    
####################################### for loop
# # Print palindrome numbers
# n=int(input("enter: "))
# for i in range(1,n+1):
#     # print(i)
#     reverse=0
#     a=i
#     for j in range(a):
#         last_digit=a%10
#         reverse=reverse*10+last_digit
#         a=a//10
#         if(a==0):
#             break
#     if reverse==i:
#         print("palindrome",i)

# # Print palindrome numbers from 100 to 999
# for i in range(100,999):
#     reverse=0
#     a=i
#     for j in range(a):
#         last_digit=a%10
#         reverse=reverse*10+last_digit
#         a=a//10
#         if (a==0):
#             break
#     if reverse==i:
#         print("palindrome",i)

# # Print prime numbers from 1 to 100.
# for i in range(1,100+1):
#     a=i
#     b=0
#     for j in range(a):
#         last=a
#         if last==0 or last==2 or last==3 or last==5 or last==7:
#             b=last
#         elif last%a==0 and last%last==0 and last%2!=0 and last%3!=0 and last%5!=0 and last%7!=0:
#             b=last
#         a=a//100
#         if a==0:
#             break
#     if b==i:
#         print("it is prime number",i)

# # Print Armstrong numbers from 100 to n.
# for i in range (1,200+1):
#     a=i
#     b=0
#     len_n=len(str(i))
#     for j in range(a):
#         last_digit=a%10
#         b=b+pow(last_digit,len_n)
#         a=a//10
#     if b==i:
#         print("armstrong",i)

# # Print Adam numbers from 100 to n.
# for i in range (1,100+1):
#     a=i
#     square_i=pow(i,2) #12>>144
#     b1=0
#     for j in range(square_i):
#         last1=square_i%10
#         b1=b1*10+last1 #441
#         square_i=square_i//10
#         if square_i==0:
#             break
#     b=0
#     for k in range(a):
#         last=a%10
#         b=b*10+last #12>>21
#         a=a//10
#         if a==0:
#             break
#     if b1==pow(b,2):
#         print(i,"adam")
    
# # Calculate student grade for each subject.
# no_of_students=3
# no_of_subjects=5
# for i in range(1,no_of_students+1):
#     enter=str(input("enter name: "))
#     a=i
#     total=0
#     for j in range(1,no_of_subjects+1):
#         subjects=int(input("enter marks: "))
#         total=total+subjects
#     print(enter)
#     print(total)

# # Find whether the given number is strong number.
# import math
# n=145
# for i in range(n,n+1):
#     a=n
#     b=0
#     for j in range(a):
#         last=a%10
#         b=b+math.factorial(last)
#         a=a//10
#         if a==0:
#             break
#     # print(n)
#     if b==n:
#         print(f"it is strong number {n}")
#     else:
#        print(f"it is not a strong number {n}") 
    
# # Multiplication table chart.
# n=10
# m=5
# for i in range (1,n+1):
#     print(f"{i}*{m}= {i*m}")
#     # print(i)