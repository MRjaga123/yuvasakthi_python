# In Python, a decorator is a function that is used to modify or extend the behavior of another function without changing its original source code.
# In simple terms, a decorator wraps another function and adds some additional functionality before or after the execution of that function.

# A decorator is a function that adds extra behavior to another function without changing its original code.
# def my_decorator(funcs):
#     def wrapper():
#         print("Before function call")
#         funcs()
#         print("After function call")
#     return wrapper
# @my_decorator
# def say_hello():
#     print("Hello, Python!")
# say_hello()
# # @my_decorator
# # def say_hellos():
# #     print("Hellos, Pythons!")
# # say_hellos()

# # Questions (decorator with argument)
# # 1.Create a decorator that prints the arguments passed to a function.
# def my_decorator(func):
#     def wrapper(name):
#         print("Before function call")
#         func(name)
#         print("After function call")
#     return wrapper
# @my_decorator
# def say_hellos(name):
#     print(f"Hello {name}")
# say_hellos("jaga")

# # 2.Write a decorator that checks if a number is positive before running the function.
# def my_decorator(func):
#     def wrapper(num):
#         if num > 0:
#             print("Before function call")
#             func(num)
#             print("After function call")
#         else:
#             print("Number is not positive. Function will not be called.")
#     return wrapper
# @my_decorator
# def print_number(num):
#     print(f"The number is: {num}")
# print_number(5)
# print_number(-3)

# Write a decorator for login authentication.



