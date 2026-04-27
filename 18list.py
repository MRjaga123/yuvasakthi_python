# Creating Lists and Accessing Elements
list1 = ["yuva", "sakthi", "academy"]
print(list1)

print(len(list1))

list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(type(list4))  

list1 = list(("apple", "mango", "orange"))
print(list1) 

print(list1[0]) 
print(list1[1]) 
print(list1[-1]) 
print(list1[2:4])
print(list1[:3]) 
print(list1[1:])
print(list1[-4:-1])  

# Check Existence and Modify List Items
list1=["yuva","system"]
if "yuva" in list1:
    print("Yes, 'yuva' is in the list")

list1[1] = "systems"  # Replace element at index 1
list1[1:3] = ["kalpana", "sakthi"]  # Replace a range
list1[1:2] = ["kalpana", "sakthi"]  # Replace one item with two
list1[1:3] = ["sakth"]  # Replace two items with one
print(list1)

# Add Items
list1=["yuva","system"]
list1.insert(2, "kalpana")  # Insert at index 2
list1.append("sakth")  # Add at the end
list1.extend(list2)  # Add list3 to list2
print(list1)

# Remove Items
list1=["yuva","system","sakthi","shaik","jaga"]
list1.remove("sakthi")  # Remove by value
list1.pop(1)  # Remove by index
list1.pop()  # Remove last item
del list1[0]  # Delete by index
# del list1  # Delete entire list
# list1.clear()  # Clear all items from list
print(list1)

# Loop Through Lists
list1=["yuva","system","sakthi"]
for x in list1:
    print(x)
for i in range(len(list1)):
    print(list1[i])
i = 0
while i < len(list1):
    print(list1[i])
    i += 1

[print(x) for x in list1]  # List comprehension loop

# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)  # Output: ['apple', 'banana', 'mango']

newlist = [x for x in fruits if "a" in x]  # Same as above using list comprehension
newlist = [x for x in fruits if x != "apple"]  # Exclude 'apple'

# Sorting and Reversing Lists
list1=["yuva","system","sakthi","shaik","jaga"]
list1.sort()  # Sort alphabetically
list1.sort(reverse=True)  # Sort in descending order
list1.sort(key=str.lower)  # Case-insensitive sort
list1.reverse()  # Reverse list order

# Copying and Joining Lists
list1=["yuva","system","sakthi","shaik","jaga"]
list2 = list1.copy()
list2 = list(list1)
list3 = list1 + list2
for x in list2:
    list1.append(x)
list1.extend(list2)  # Add list2 items to list1

##### exercise
# Exercise 1: Reverse a given list in Python
aList = [100, 200, 300, 400, 500]
aList.reverse()
print(aList)

# Exercise 2: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3=[]
for i,ii in enumerate(list1):
    list3.append(list1[i]+list2[i])
print(list3)

# Exercise 3: Given a Python list of numbers. Turn every item of a list into its square
aList = [1, 2, 3, 4, 5, 6, 7]
blist=[]
for i in aList:
    blist.append(pow(i,2))
print(blist)

# Exercise 4: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3=[]
for i in range (len(list1)):
    for j in range (len(list2)):
        list3.append(list1[i]+list2[j])
print(list3)

# Exercise 5: Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.reverse()
for i in range(len(list1)):
    print(list1[i],list2[i])
    
# Exercise 6: Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
for i in list1:
    if i=="":
        list1.remove(i)
print(list1)

# Exercise 7: Add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

# Exercise 8: Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look like the following list
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list2 = ["h", "i", "j"]
list1[2][1][2].extend(list2)
print(list1)

# Exercise 9: Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
list1 = [5, 10, 15, 20, 25, 50, 20]
if 20 in list1:
    idx=list1.index(20)
    list1[idx]=200   
print(list1)

# Exercise 10: Given a Python list, remove all occurrence of 20 from the list
list1 = [5, 20, 15, 20, 25, 50, 20]
for i,ii in enumerate(list1):
    if ii==20:
        list1.pop(i)
print(list1)
