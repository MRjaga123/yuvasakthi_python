# A set is a collection that is unordered, unindexed, and contains no duplicate elements. Sets are defined using curly braces {}.

# 1. Creating and Accessing Sets
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
for x in thisset:
    print(x)
print("banana" in thisset)  # Membership test

# 2. Adding and Updating Items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
thisset.update(["orange", "mango", "grapes"])
print(thisset)

# 3. Removing Items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
thisset.discard("banana")
thisset.pop()  # Removes a random item
# thisset.clear()
# del thisset
print(thisset)

# 4. Set Operations
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set1.update(set2)
print(set1)

# 5. Set Comparisons
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y) #common
print(z) 
result = x.intersection({"banana", "cherry"}, {"cherry"})
print(result)

z = x.difference(y) 
print(z)

z = x.isdisjoint({"facebook", "microsoft"})
print(z)

z = {"a", "b", "c"}.issubset({"a", "b", "c", "d"})
print(z)

z = {"a", "b", "c", "d"}.issuperset({"b", "c"})
print(z)

z = x.symmetric_difference(y)
print(z)

##### Exercise
# Exercise 1: Add a list of elements to a given set
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
sampleSet.update(sampleList)
print(sampleSet)

# Exercise 2: Return a new set of identical items from a given two set
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))

# Exercise 3: Returns a new set with all items from both sets by removing duplicates
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.union(set2))

# Exercise 4: Given two Python sets, update the first set with items that exist only in the first set and not in the second set.
set1 = {10, 20, 30}
set2 = {20, 40, 50}
print(set1.difference(set2))

# Exercise 5: Remove items 10, 20, 30 from the following set at once
set1 = {10, 20, 30, 40, 50}
list1=[10,20,30]
set1.difference_update(list1)
print(set1)

# Exercise 6: Return a set of all elements in either A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.symmetric_difference(set2))

# Exercise 7: Check if two sets have any elements in common. If yes, display the common elements.
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
print(set1.intersection(set2))

# Exercise 8: Update set1 by adding items from set2, except common items
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.symmetric_difference(set2))

# Exercise 9: Remove items from set1 that are not common to both set1 and set2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print(set1)
