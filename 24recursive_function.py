# A recursive function is a function that calls itself during its own execution. It solves a complex problem by breaking it down into smaller, simpler sub-problems of the same type, until it reaches a simple base case that can be solved directly.
# Types of Recursion
    # 1. Direct Recursion-Function calls itself directly
    # 2. Indirect Recursion-Function calls another function, which calls the first function
    # 3. Tail Recursion-Recursive call is the last operation
    # 4. Non-Tail Recursion-Recursive call is not the last operation
    
# # Example: 
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))
# print(factorial(4))
# print(factorial(3))
# print(factorial(2))
# print(factorial(1))

# # 1.Sum of Nature Number?
# def sum_n(n):
#     if n==0:
#         return 0
#     return n+sum_n(n-1)
# print(sum_n(5))

# # 2.Power of a Number (X^N)
# def power_x(x,n):
#     if n==0:
#         return 1
#     return x*power_x(x,n-1)
# print(power_x(5,2))

# # 3.Reverse a String
# def reverse_s(s):
#     if len(s)==0:
#         return s
#     return reverse_s(s[1:])+s[0]
# print(reverse_s("hello"))

# # 4.Count Digits in a Number
# def count_n(n):
#     if n==0:
#         return 0
#     return 1+count_n(n//10)
# print(count_n(12354))

# # fibonacci series
# def fibonacci(n):
#     # if n<=0:
#     #     return 0
#     if n<=1:
#         return 1
#     return(fibonacci(n-1)+fibonacci(n-2))    
# print(fibonacci(7))

# # 6.Palindrome Check
# def palindrome_n(n):
#     if len(n)<=1:
#         return True
#     if n[0]!=n[-1]:
#         return False
#     return palindrome_n(n[1:-1])
# print(palindrome_n("madam"))



