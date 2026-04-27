# n=5
# a=[]
# for i in range(1,n+1):
#     x=int(input("enter: "))
#     a.append(x)
# print(a)

##### 1
# n=10
# a=[]
# for i in range(1,n+1):
#     x=int(input("enter: "))
#     a.append(x)
# print(a[3],a[5])

##### 2
# n=10
# a=[]
# for i in range(1,n+1):
#     x=int(input("enter: "))
#     a.append(x)
# print(a[0],a[-1])

##### 3
# n=10
# a=[]
# for i in range(1,n+1):
#     x=int(input("enter: "))
#     a.append(x)
# a[2]=50
# print(a)

##### 4 
# n=10
# a=[]
# for i in range(1,n+1):
#     x=int(input("enter: "))
#     a.append(x)
# temp=a[0]
# a[0]=a[-1]
# a[-1]=temp
# print(a)

##### 5
# n=10
# a=[]
# for i in range(1,n+1):
#     x=int(input("enter a: "))
#     a.append(x)
# b=int(input("enter b: "))
# if b in a:
#     print("yes")
# else:
#     print("no")

##### 6
# n=10
# a=[]
# for i in range(1,n+1):
#     x=int(input("enter a: "))
#     a.append(x)
# b=int(input("enter b: "))
# if b in a:
#     print(a.index(b))
# else:
#     print("no")
# print(a)

##### 7
# n=10
# a=[]
# for i in range(1,n+1):
#     x=int(input("enter a: "))
#     a.append(x)
# b=int(input("enter b: "))
# if b in a:
#     b1=b
# else:
#     print("no")
# a1=[]
# for i in a:
#     if i != b1:
#         a1.append(i)
# print(a1)

##### 8
# n=10
# a=[]
# for i in range(1,n+1):
#     x=int(input("enter a: "))
#     a.append(x)
# a1=0
# for i in a:
#         a1=a1+i
# print("total: ",a1)

##### 9
# n=10
# a=[]
# for i in range(1,n+1):
#     x=int(input("enter a: "))
#     y=int(input("enter b: "))
#     a.append(x+y)
# print("total_x/y: ",a)

##### 10
# n=5
# a=[]
# for i in range(1,n+1):
#     x=int(input("enter a: "))
#     a.append(x)
# # print(a)
# a1=[]
# index=-1
# for i in a:
#     a1.append(a[index])
#     index=index-1
# print(a1)

##### 11
# n=5
# a=[]
# for i in range(1,n+1):
#     x=int(input("enter a: "))
#     a.append(x)
# for i,ii in enumerate(a):
#     print(i,len(a))
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)

##### 12
# n=5
# a=[]
# for i in range(1,n+1):
#     x=int(input("enter: "))
#     a.append(x)
# for i,ii in enumerate(a):
#     for j in range (i+1,len(a)):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)

##### 13
# n=5
# a=[]
# for i in range (1,n+1):
#     x=int(input("enter: "))
#     a.append(x)
# # print(a)
# for i,ii in enumerate(a):
#     for j in range(i+1,len(a)):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a[0])#largest number

##### 14
# n=5
# a=[]
# for i in range (1,n+1):
#     x=int(input("enter: "))
#     a.append(x)
# # print(a)
# for i,ii in enumerate(a):
#     for j in range (i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a[0])#smallest number

##### 15
# n=5
# a=[]
# for i in range(1,n+1):
#     x=int(input("enter: "))
#     a.append(x)
# # print(a)
# for i,ii in enumerate(a):
#     for j in range (i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)
# print(a[-2])#second largest number in ascending

##### 16
# n=5
# a=[]
# for i in range (1,n+1):
#     x=int(input("enter: "))
#     a.append(x)
# for i,ii in enumerate(a):
#     for j in range (i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)
# print(a[1])#second smallest number in ascending

##### 17
# n=5
# a=[]
# for i in range (1,n+1):
#     x=int(input("enter: "))
#     a.append(x)
# for i,ii in enumerate(a):
#     for j in range (i+1,len(a)):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)
# print(a[1])#second largest number in descending

##### 18
# n=5
# a=[]
# for i in range (1,n+1):
#     x=int(input("enter: "))
#     a.append(x)
# for i,ii in enumerate(a):
#     for j in range (i+1,len(a)):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)
# print(a[-2])#second smallest number in descending

##### 19
# n=5
# a=[]
# for i in range (1,n+1):
#     x=int(input("enter: "))
#     a.append(x)
# for i,ii in enumerate(a):
#     for j in range (i+1,len(a)):
#         if a[i]==a[j]:
#             print("duplicate values: ",a[i])
#     # print(i)

##### 20
# n=5
# a=[]
# for i in range (1,n+1):
#     x=str(input("enter: "))
#     a.append(x)
# for i,ii in enumerate(a):
#     for j in range (i+1,len(a)):
#         if a[i]==a[j]:
#             print("duplicate values: ",a[i])
#     # print(i)

##### 21
# n=5
# a=[]
# a1=[]
# duplicates=[]
# for i in range (1,n+1):
#     x=int(input("enter x: "))
#     a.append(x)
#     y=int(input("enter y: "))
#     a1.append(y)
# # duplicates=set(a) & set(a1)
# for i in a:
#     if i in a1 and i not in duplicates:
#         duplicates.append(i)
# print(duplicates)

##### 22
# n=5
# a=[]
# a1=[]
# duplicates=[]
# for i in range (1,n+1):
#     x=str(input("enter x: "))
#     a.append(x)
#     y=str(input("enter y: "))
#     a1.append(y)
# for i in a:
#     if i in a1 and i not in duplicates:
#         duplicates.append(i)
# print(duplicates)

##### 23
# n=5
# a=[]
# a1=[]
# for i in range (1,n+1):
#     x=int(input("enter x: "))
#     a.append(x)
# for i in a:
#     if i not in a1:
#         a1.append(i)
# print(a1)

##### 24
# n=5
# a=[]
# a1=[]
# for i in range (1,n+1):
#     x=int(input("enter x: "))
#     a.append(x)
#     y=int(input("enter y: "))
#     a1.append(y)
# if a==a1:
#     print("equality of two arrays.")
# else:
#     print("not equality of two arrays.")

##### 25
# n=5
# a=[]
# a1=[]
# for i in range (1,n+1):
#     x=int(input("enter x: "))
#     if x==0:
#         a1.append(x)
#     else:
#         a.append(x)
# a.extend(a1)
# print(a)

##### 26
# n=5
# a=[]
# for i in range (1,n+1):
#     x=int(input("enter x: "))
#     a.append(x)
# count_even=0
# count_odd=0
# for i in a:
#     if i%2==0:
#         count_even=count_even+1
#     else:
#         count_odd=count_odd+1
# print(f"even :{count_even}, odd :{count_odd}")

##### 27
# n=5
# a=[]
# for i in range (1,n+1):
#     x=int(input("enter x: "))
#     a.append(x)
# for i,ii in enumerate(a):
#     for j in range (i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# a.pop(0)
# a.pop()
# sum=0
# for i in a:
#     sum=sum+i
# print(f"average: {sum/len(a)}")

##### 28
# n=5
# a=[]
# for i in range (1,n+1):
#     x=int(input("enter x: "))
#     a.append(x)
# if -1 in a or 0 in a:
#     print("it is valid")
# else:
#     print("it is invalid")

##### 29
# n=5
# a=[]
# for i in range (1,n+1):
#     x=int(input("enter x: "))
#     a.append(x)
# leader=[]
# for i,ii in enumerate(a):
#     for j in range (i+1,len(a)):
#         if a[i]>a[j]:
#             if a[i] not in leader:
#                 leader.append(a[i])
# print(leader)

##### 30
# n=5
# a=[]
# for i in range (1,n+1):
#     x=int(input("enter x: "))
#     a.append(x)
# one=[]
# result=[]
# for i in a:
#     # print(i)
#     if i==0:
#         result.append(i)
#     elif i==1:
#         one.append(i)
# result.extend(one)
# print(result)

