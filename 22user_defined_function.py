### standard function defined with def.

#1.No argument/no return type
def say_hello1():
    print("hi this is jaga")
say_hello1()

#2.argument/no return type
def say_hello2(name):
    print(f"hi this is {name}")
say_hello2("alice")

#3.no argument/return type
def say_hello3():
    return "jaga"
a=say_hello3()
print(a)

#4.argument/return type
def say_hello4(name):
    return name
b=say_hello4("jaga")
print(b)

##argument type 
# 1.positional argument
def say_hello(name,location):
    print(f"hi i am {name} from {location}")
say_hello("jaga","mannai")

# 2.keyword argument
def say_hello(name,location):
    print(f"hi i am {name} from {location}")
say_hello(location="mannai",name="jaga")

# 3.default argument
def say_hello(name,location="mannai"):
    print(f"hi i am {name} from {location}")
say_hello("jaga")

# 4.arbitary argument
# *args
def say_hello(*numbers):
    print(sum(numbers))
say_hello(1,2,3,4,5)

# **kwargs
def say_hello(**info):
    print(info)
say_hello(name="jaga",location="mannai")