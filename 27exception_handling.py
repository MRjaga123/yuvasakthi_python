##### error handling
#try #except #else #finally #raise

# # syntax error 
# a=10
# b=20
# if (a<b)
#     print("a is big")
    
# # type error
# try:
#     a=10
#     b="jaga"
#     c=a+b
#     print(c)
# except TypeError as t:
#     print(t)

# # name error 
# try:
#     a=10
#     b=20
#     c=a+d
#     print(c)
# except NameError as n:
#     print(n)

# # index error 
# try:
#     indexes=[1,2,True]
#     print(indexes[3])
# except IndexError as i:
#     print(i)

# # key error 
# try:
#     sample_dict={"name":"jaga","age":21}
#     emp_name=sample_dict["name"]
#     emp_year=sample_dict["year"]
#     print(emp_name)
#     print(emp_year)
# except KeyError as k:
#     print(k)

# # value error 
# try:
#     i=int(input("enter in int: "))
#     print(i)
# except ValueError as v:
#     print(v)

# # attribute error 
# try:
#     tuples=(1,2,True)
#     ins=int(input("enter: "))
#     tuples.append(ins)
#     print(tuples)
# except AttributeError as a:
#     print(a)

# # IO error
# try:
#     f=open("jaga.pdf")
#     f.write("hi")
# except IOError as io:
#     print(io)
    
# # zero division error 
# try:
#     a=10
#     b=0
#     print(a/b)
# except ZeroDivisionError as z:
#     print(z)

# # import error 
# try:
#     import tensorflow
# except ImportError as i:
#     print(i)

##### try except else finally
# try:
#     print("hi")
# except:
#     print("error")
# else:
#     print("nothing")
# finally:
#     print("bye")
    
# # custom exception
# class invalidage(Exception):
#     #print("you are invalid")
#     pass
# def verifyage():
#     verifedyage=18
#     try:
#         age=int(input("enter age :  "))
#         if age<verifedyage:
#             print("you are invalid")
#             raise invalidage
#         else:
#             print("you are valid")
#     except Exception as e:
#         print(e)
# verifyage()    

# task1
class Invalid_password(Exception):
    pass
def check_password(use=1,max=3):
    correct_password=12345
    password=int(input("enter password: "))
    try:
            if password!=correct_password:
                print("password is incorect")
                raise Invalid_password
            else:
                print("welcome")
    except Exception as e:
        if use<max:
            print(e)
            check_password(use=use+1,max=3)
        else:
            print("phone is locked")
check_password()
        