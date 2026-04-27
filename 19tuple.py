# Tuples are ordered collections that are immutable (unchangeable) once defined.

# 1.Creating and Accessing Tuples
tuple1 = ("apple", "banana", "cherry")
print(tuple1)
print(len(tuple1))

# 2.Single Element Tuple
tuple1 = ("apple",)
print(type(tuple1))
tuple1 = ("apple")  # Not a tuple
print(type(tuple1))  # Output: <class 'str'>

# 3.Tuple with Mixed Data Types
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# 4.Tuple Constructor
tuple1 = tuple(("apple", "banana", "cherry"))
print(tuple1)

# 5.Tuple Indexing and Slicing
tuple1 = ("apple", "banana", "cherry")
print(tuple1[1])
print(tuple1[-1])
tuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple1[2:5])
print(tuple1[:4])
print(tuple1[2:])
print(tuple1[-4:-1])

# 6.Check for Item
if "apple" in tuple1:
    print("Yes, 'apple' is in the fruits tuple")

# 7.Change Tuple Values (via list conversion)
x = ("apple", "banana", "cherry")
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)

# 8.Add/Remove Items by Conversion
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# 9.Delete Tuple
thistuple = ("apple", "banana", "cherry")
del thistuple

# 10.Unpacking a Tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# 11.Using Asterisk for Variable Capture
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

# 12.Loop Through Tuple
tuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
for x in tuple1:
  print(x)
for i in range(len(tuple1)):
  print(tuple1[i])
I = 0
while I < len(tuple1):
  print(tuple1[I])
  I += 1

# 13.Join and Multiply Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)


##### Exercise
# Exercise 1: Reverse the following tuple
aTuple = (10, 20, 30, 40, 50)
x=list(aTuple)
x.reverse()
aTuple=tuple(x)
print(aTuple)

# Exercise 2: Access value 20 from the following tuple
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
if 20 in aTuple[1]:
    print("it is valid")
else:
    print("it is invalid")

# Exercise 3: Create a tuple with single item 50
list1=[]
list1.append(50)
tuple1=tuple(list1)
print(tuple1)

# Exercise 4: Unpack the following tuple into 4 variables
aTuple = (10, 20, 30, 40)
(a,b,c,d)=aTuple
print(a)
print(b)
print(c)
print(d)

# Exercise 5: Swap the following two tuples
tuple1 = (11, 22)
tuple2 = (99, 88)
temp=tuple1
tuple1=tuple2
tuple2=temp
print(tuple1)
print(tuple2)

# Exercise 6: Copy element 44 and 55 from the following tuple into a new tuple
tuple1 = (11, 22, 33, 44, 55, 66)
list1=[]
for i in tuple1:
    if i ==44 or i==55:
        list1.append(i)
tuple2=tuple(list1)
print(tuple2)

# Exercise 7: Modify the first item (22) of a list inside a following tuple to 222
tuple1 = (11, [22, 33], 44, 55)
list1=list(tuple1)
for i,ii in enumerate(list1):
    if isinstance(ii,list):
        for j,iii in enumerate(ii):
            # print(j,iii)
            if iii==22:
                list1[i][j]=222
tuple1=tuple(list1)
print(tuple1)

# Exercise 8: Sort a tuple of tuples by 2nd item
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
list1=list(tuple1) #[('a', 23), ('b', 37), ('c', 11), ('d', 29)]
n=len(list1)
for i in range (n):
    # print(i)
    for j in range(0,n-1) :
        # print(j)
        if list1[j][1]>list1[j+1][1]:
            # print("yes")
            list1[j],list1[j+1]=list1[j+1],list1[j]                  
print(list1)

# Exercise 9: Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
count=0
for i in tuple1:
    if i==50:
        count=count+1
print(count)  

# Exercise 10: Check if all items in the following tuple are the same
tuple1 = (45, 45, 45, 45)
len_n=len(tuple1)
count=0
for i in tuple1:
    if i==tuple[0]:
        count=count+1
if count==len_n:
    print("it is valid")
else:
    print("it is invalid")