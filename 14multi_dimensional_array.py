# n=2
# a=[]
# for i in range(n):
#     b=[]
#     for j in range(n):
#         x=int(input("enter: "))
#         b.append(x)
#     a.append(b)
# print(a)
# print(a[0][1])

##### 1 transpose matrix
# n=3
# a=[]
# for i in range(n):
#     b=[]
#     for j in range (n):
#         x=int(input("enter x: "))
#         b.append(x)
#     a.append(b)
# # print(a)
# # row=len(a[0])
# # column=len(a)
# for i in range (n):
#     tranpose=[]
#     for j in range (n):
#         # a[i][j]=a[j][i]
#         if a[i][j]:
#             tranpose.append(a[j][i])
#         # print(i,j)
#     print(tranpose)
# # print(a)

##### 2 Symmetric matrix
# n=2
# a=[]
# for i in range (n):
#     b=[]
#     for j in range (n):
#         x=int(input("enter: "))
#         b.append(x)
#     a.append(b)
# print("a:",a)
# transpose=[]
# for i in range(n):
#     trans=[]
#     for j in range (n):
#         if a[i][j]:
#             trans.append(a[j][i])
#     transpose.append(trans)
# print("transpose:",transpose)
# if transpose==a:
#     print("it is a symmetric matrix")
# else:
#     print("it is not a symmetric matrix")

##### 3  Identity Matrix
# n=2
# a=[]
# for i in range (n):
#     b=[]
#     for j in range (n):
#         x=int(input("enter: "))
#         b.append(x)
#     a.append(b)
# print("a:",a)
# if a[0][0]==a[1][1]:
#     print("it is a identity matrix")
# else:
#     print("it is not a identity matrix")

##### 4  Matrix multiplication
# n=2
# a=[]
# for i in range (n):
#     a1=[]
#     for j in range (n):
#         x=int(input("enter: "))
#         a1.append(x)
#     a.append(a1)
# print("a:",a)
# b=[]
# for i in range (n):
#     b1=[]
#     for j in range (n):
#         x=int(input("enter: "))
#         b1.append(x)
#     b.append(b1)
# print("b:",b)
# multiplication=[]
# for i in range (n):
#     multi=[]
#     for j in range (n):
#         if a[i][j] and b[i][j]:
#             multi.append(a[i][j]*b[i][j])
#     multiplication.append(multi)
# print(multiplication)

##### 5 Matrix multiplication
# n=2
# a=[]
# for i in range (n):
#     a1=[]
#     for j in range (n):
#         x=int(input("enter: "))
#         a1.append(x)
#     a.append(a1)
# print("a:",a)
# b=[]
# for i in range (n):
#     b1=[]
#     for j in range (n):
#         x=int(input("enter: "))
#         b1.append(x)
#     b.append(b1)
# print("b:",b)
# multiplication1=[]
# for i in range (n):
#     multi=[]
#     for j in range (n):
#         multi1=0
#         for k in range (n):
#             print(i,j,k)
#             multi1=multi1+(a[i][j]*b[k][j])
#         multi.append(multi1)
#     multiplication1.append(multi)
# print(multiplication1)
