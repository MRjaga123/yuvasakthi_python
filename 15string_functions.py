#using single quotes
name='i am jaga'
print(name)

#using double quotes
name="i am jaga"
print(name)

#using triple quotes
name='''hello
i am jaga'''
print(name)

##Python String Methods
#1.capitalize()
txt = "hello, and welcome to my world."
x=txt.capitalize()
print(x)

#2.casefold()
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

#3.center()
txt = "banana"
x = txt.center(20)
print(x)

#4.count()
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

#5.endswith()
txt = "Hello, welcome to my world."
x = txt.endswith(".")
y = txt.endswith("world.")
print(x,y)

#6.expandtabs()
txt = "H\te\tl\tl\to"
x = txt.expandtabs(2)
print(txt.expandtabs())
print(x) 

#7.encode()
txt = "My name is Ståle"
x = txt.encode()
print(x)

#8.find()
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
x = txt.find("e")
print(x)
x = txt.find("e", 5, 10)
print(x)
print(txt.find("q"))

#9.format()
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

#10.index()
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)  # Output: 7
x = txt.index("e")
print(x)  # Output: 1
x = txt.index("e", 5, 10)
print(x)

#11.isalnum()
txt = "Company12"
x = txt.isalnum()
print(x)

#12.isalpha()
txt = "CompanyX"
x = txt.isalpha()
print(x) 

#13.isupper()
txt = "THIS IS NOW!"
x = txt.isupper()
print(x) 

#14.join()
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

#15.lower()
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

#16.strip()/lstrip()/rstrip()
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

#17.replace()
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

#18.split()
txt = "welcome to the jungle"
x = txt.split()
print(x)

#19.splitlines()
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x) 

#20.upper()
txt = "Hello my friends"
x = txt.upper()
print(x)