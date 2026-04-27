##### 1
# n=5
# for i in range(1,n+1):
#     # print(i)
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

##### 2  
# n=5
# for i in range(n,0,-1):
#     for j in range(n,i-1,-1):
#         print(j,end="")
#     print()

##### 3
# n=5
# for i in range(1,n+1):
#     # print(i)
#     for j in range (i,0,-1):
#         print(j,end="")
#     print()

##### 4
# n=4
# a=1
# for i in range(1,n+1):
#     # print(i)
#     for j in range(1,i+1):
#         print(a,end="")
#         a=a+1
#     print()

##### 5
# n=5
# for i in range(1,n+1):
#     # print(i)
#     for k in range (n,i-1,-1):
#         print(".",end="")
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()

##### 6
# n=5
# for i in range (n,0,-1):
#     a=i
#     for j in range (i,a-i,-1):
#         print(j,end="")
#     print()

##### 7
# n=5
# a=1
# for i in range (1,n+1):
#     a=i
#     for j in range(a,a+n):
#         if j%2!=0:
#             print("1",end="")
#         elif j%2==0:
#             print("0",end="")
#     print()
    
##### 8
# n=5
# for i in range(1,n+1):
#     # print(i)
#     for j in range(1,i+1):
#         if j%2!=0:
#             print("1",end="")
#         elif j%2==0:
#             print("0",end="")
#     print()

##### 9
# n=5
# for i in range(1,n+1):
#     # print(i)
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# n=4
# for i in range (n,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

##### 10
# n=5
# i=1
# for i in range (1,n+1):
#     # print(i)
#     for j in range(1,i+1):
#         print(i,end="")
#     print()

##### 11
# n=5
# for i in range(1,n+1):
#     # print(i)
#     for j in range(1,i+1):
#         print(" * ",end="")
#     print()

##### 12
# n=5
# for i in range (n,0,-1):
#     # print(i)
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

##### 13
# n=5
# a=1
# for i in range(n,0,-1):
#     # print(i)
#     for j in range (n,a-1,-1):
#         print(j,end="")
#     a=a+1
#     print()

##### 14
# n=5
# for i in range(1,n+1):
#     # print(i)
#     for j in range(i,n+1):
#         print(".",end="")
#     for k in range(1,i+1):
#         print(k,end="")
#     print()

##### 15
# n=5
# i=1
# # while (i<=n):
# for i in range(1,n+1):
#     # print(i)
#     # j=5
#     # while (j>=i):
#     for j in range(i,n+1):
#         print(j,end="")
#     print()

##### 16
# n=5
# a=5
# for i in range(1,n+1):
#     # print(i)
#     for j in range(a,6):
#         print(j,end="")
#     a=a-1
#     print()


##### 17
# n=5
# i=n
# a=1
# while(i>=1):
#     # print(i)
#     j=n
#     x=a
#     while(j>=i):
#         print(x,end="")
#         x=(j+x)-1
#         j=j-1
#     a=a+1
#     i=i-1
#     print()

##### 18
# n=5
# i=1
# for i in range(1,n+1):
#     # print(i)
#     for j in range(i,n+1):
#         print(" ",end="")
#     for k in range(i,i+1):
#         print("*",end="")
#     for l in range (2,i+1):
#         print(" ",end="")
#     for m in range(2,i+1):
#         print(" ",end="")
#     for o in range (i,i+1):
#         if i>1:
#             print("*",end="")
#         else:
#             print("",end="")
#     print() 
# n=4
# i=1
# for i in range(1,n+1):
#     # print(i)
#     for j in range(1,i+2):
#         print(" ",end="")
#     for k in range(i,i+1):
#         print("*",end="")
#     for l in range(i,n):
#         print(" ",end="")
#     for m in range (n,i,-1):
#         print(" ",end="")
#     for o in range (i,i+1):
#         if o<4:
#             print("*",end="")
#     print()    

##### 19
# n=5
# i=1
# for i in range(1,n+1):
#     # print(i)
#     for j in range(i,n+1):
#         print(" ",end="")
#     for k in range(i,i+1):
#         print("*",end="")
#     for l in range (2,i+1):
#         print(" ",end="")
#     for m in range(2,i+1):
#         print(" ",end="")
#     for o in range (i,i+1):
#         if i>1:
#             print("*",end="")
#         else:
#             print("",end="")
#     print() 
# n=12
# i=1
# for i in range (1,n+1):
#     print("*",end="")  

##### 20
# n=5
# for i in range (1,n+1):
#     # print(i)
#     for j in range (n+1,i,-1):
#         print(" ",end="")
#     for k in range (1,i+1):
#         print(k,end="")
#     for l in range (i-1,0,-1):
#         if i>1:
#             print(l,end="")
#     print() 
# n=4
# a=1
# for i in range (n,0,-1):
#     # print(i)
#     for j in range (0,a+1):
#         print(" ",end="")
#     a=a+1
#     for k in range(1,i+1):
#         print(k,end="")
#     for l in range (i-1,0,-1):
#         print(l,end="")
#     print()

##### 21
# n=5
# for i in range (1,n+1):
#     # print(i)
#     for j in range (n+1,i,-1):
#         print(" ",end="")
#     for k in range (1,i+1):
#         print("*","",end="")
#     print()
# n=5
# a=1
# for i in range (1,n+1):
#     # print(i)
#     for j in range (0,i+1):
#         print(" ",end="")
#     for k in range (n,i,-1):
#         print("*","",end="")
#     print()

##### 22
# n=11
# for i in range (1,n+1):
#     print("*",end="")
# print() 
# n=5
# a=1
# for i in range (1,n+1):
#     # print(i)
#     for j in range (1,i+1):
#         print(" ",end="")
#     for k in range (n+1,i,-1):
#         print("*","",end="")
#     print()

##### 23
# a=["A","B","C","D","E"]
# n=len(a)
# for i in range (0,n):
#     for j in range (0,i+1):
#         print(a[j],end="")
#     print()

#####24
# n=5
# for i in range(1,n+1):
#     for j in range (1,6):
#         print("*",end="")
#     print()

##### 25
# n=5
# i=1
# for i in range (1,n+1):
#     for j in range (i,n+1):
#         print(" ",end="")
#     for k in range (1,i+1):
#         print("*",end="")
#     for l in range (2,i+1):
#         print("*",end="")
#     print()
# n=4
# i=1
# # while (n1>=i1):
# for i in range(1,n+1):
#     # print(i)
#     for k in range (1,i+1):
#         print(" ",end="")
#     for j in range (i,n+1):
#         print("*",end="")
#     for l in range (i,n+1):
#         print("*",end="")
#     print()

##### 26
# a=["A","B","C","D","E","F"]
# n=len(a)
# for i in range (1,n+1):
#     # print(i)
#     for j in range (n,i,-1):
#         print(" ",end="")
#     for k in range (i,i+1):
#         print(a[k-1],end="")
#     for l in range (2,i+1):
#         print(".","",end="")
#     for m in range (i,i+1):
#         if m>1:
#             print(a[m-1],end="")
#     print()
# n=len(a)-1
# A=1
# for i in range (n,0,-1):
#     # print(i,end="")
#     for j in range (0,A):
#         print(".",end="")
#     A=A+1
#     for k in range (i,i+1):
#         print(a[k-1],end="")
#     for m in range (A,n+1):
#         print(".","",end="")
#     for l in range (i,i+1):
#         if l>1:
#             print(a[l-1],end="")
#     print()

##### 27
# n=11
# i=1
# for i in range (1,n+1):
#     print("*",end="")
# print() 
# n=5
# a=1
# for i in range (1,n+1):
#     # print(i)
#     for j in range (1,i+1):
#         print(" ",end="")
#     for k in range (i,i+1):
#         print("*","",end="")
#     for l in range (i+2,n+1):
#         print(" ","",end="")
#     for m in range(i,i+1):
#         if i<=4:
#             print("*","",end="")
#     print()
# n=5
# a=1
# for i in range(1,n+1):
#     # print(i)
#     for j in range (n,a,-1):
#         print(".",end="")
#     a=a+1
#     for k in range(i,i+1):
#         print("*","",end="")
#     for l in range(2,i+1):
#         print(".","",end="")
#     for l in range(i,i+1):
#         print("*","",end="")
#     print()
# n=11
# for i in range (1,n+1):
#     print("*",end="")
    
##### 28
# n=5
# for i in range(1,n+1):
#     print("*",end="")
# print()
# n=3
# for i in range (1,n+1):
#     for j in range(i,i+1):
#         print("*",end="")
#     for k in range(i,i+3):
#         print(" ",end="")
#     for l in range (i,i+1):
#         print("*",end="")
#     print()
# n=5
# for i in range (1,n+1):
#     print("*",end="")

##### 29
# a=["A","B","C","D","E","F"]
# n=len(a)-1
# for i in range(0,n+1):
#     # print(a[i])
#     for j in range(n,i,-1):
#         print(" ",end="")
#     for k in range(0,i+1):
#         print(a[k],"",end="")
#     print()

##### 30 
# n=6
# for i in range (1,n+1):
#     # print(i)
#     for j in range (1,i+1):
#         print("*",end="")
#     print()

##### 31
# a=["A","B","C","D","E"]
# n=len(a)-1
# for i in range(0,n+1):
#     for j in range(0,i+1):
#         print(a[i],end="")
#     print()

##### 32
# a=["A","B","C","D","E"]
# n=len(a)
# for i in range (n,0,-1):
#     # print(a[i-1],i)
#     for j in range(0,i):
#         print(a[j],end="")
#     print()

##### 33
# n=3
# for i in range (1,n+1):
#     for j in range (i,n+1):
#         print(" ",end="")
#     for k in range (i,i+1):
#         print("*",end="")
#     for l in range (2,i+1):
#         print(" ","",end="")
#     for m in range (i,i+1):
#         if i>1:
#             print("*",end="")
#     print()
# n=8
# for i in range (1,n+1):
#     print("*",end="")

##### 34
# n=6
# for i in range (n,0,-1):
#     for j in range(0,i):
#         print("*",end="")
#     print()

##### 35
# n=5
# for i in range (1,n+1):
#     for j in range (i,i+1):
#         print("*",end="")
#     for k in range (1,i+1):
#         print(" ",end="")
#     for l in range (i,i+1):
#         if i>1:
#             print("*",end="")
#     print()
# n=6
# for i in range(0,n+1):
#     print("*",end="")


##### 36
# n=5
# for i in range (1,n+1):
#     for j in range(n+1,i,-1):
#         print(" ",end="")
#     for k in range (i,i+1):
#         print("*",end="")
#     for l in range (2,i+1):
#         print(" ","",end="")
#     for o in range (i,i+1):
#         if i>1:
#             print("*",end="")
#     print()
# n=5
# for i in range (0,n+1):
#     print("*","",end="")
#     # print()

##### 37
# n=5
# for i in range (1,n+1):
#     for j in range (1,2):
#         print(j,end="")
#     for k in range (2,i+1):
#         if i<5:
#             print(" ",end="")
#         if i>=5:
#             print(k,end="")
#     for l in range (i,i+1):
#         if i>1 and i<5:
#             print(l,end="")
#     print()

##### 38 
# n=5
# for i in range (1,n+1):
#     # print(i)
#     for j in range (i,i+1):
#         print(j,end="")
#     for k in range (i,n):
#         if (i<=1 and k<5 and k>1):
#             print(k,end="")
#         print(" ",end="")
#     for l in range (i,i+1):
#         if i<5:
#             print(5,end="")
#     print()

##### 39
# n=5
# for i in range (1,n+1):
#     for j in range (n+1,i,-1):
#         print(".",end="")
#     for k in range (1,i+1):
#         print(k,end="")
#     for l in range (i-1,0,-1):
#         print(l,end="")
#     print()

##### 40
# n=5
# i=1
# for i in range (1,n+1):
#     for j in range (n+1,i,-1):
#         print(" ","",end="")
#     for k in range (1,i+1):
#         print("*","",end="")
#     for l in range (2,i+1):
#         print("*","",end="")
#     print()

##### 41
# n=5
# for i in range (1,n+1):
#     for j in range (1,i+1):
#         print(j,"",end="")
#     print()

##### 42
# n=5
# i=n
# a=1
# a1=1
# while(i>=1):
#     # print(i)
#     k=1
#     while (k<=i):
#         print(" ",end="")
#         k=k+1
#     j=n
#     x=a
#     while(j>=i):
#         print(x,end="")
#         x=x+1
#         j=j-1
#     l=n
#     x1=x-2
#     while (l>=i+1):
#         print(x1,end="")
#         x1=x1-1
#         l=l-1
#     a1=a1+1
#     a=a+1
#     i=i-1
#     print()

##### 43
# n=5
# for i in range (1,n+1):
#     for j in range (1,i+1):
#         print(j,end="")
#     for k in range (i-1,0,-1):
#         print(k,end="")
#     print()

##### 44
# n=5
# for i in range (1,n+1):
#     # print(i,end="")
#     for j in range (n+1,i,-1):
#         print("*","",end="")
#     for k in range (1,i+1):
#         if (i>=1):
#             print(i,"",end="")
#         print("*","",end="")
#     for l in range (n,i,-1):
#         print("*","",end="")
#     print()

##### 45
# n=6
# for i in range (1,n+1):
#     # print(i)
#     for j in range (1,i+1):
#         print(" ",end="")
#     for k in range (n+1,i,-1):
#         print("*","",end="")
#     print()

##### 46
# n=5
# for i in range (n,0,-1):
#     for j in range (1,i+1):
#         print(j,end="")
#     print()

##### 47
# n=5
# for i in range (1,n+1):
#     # # print(i)
#     for j in range (n+1,i,-1):
#         print(" ",end="")
#     for k in range (1,2):
#         print(k,end="")
#     for l in range (2,i+1):
#         print(" ",end="")
#         if i>=5:
#             print(l,end="")
#     for m in range (2,i+1):
#         print(" ",end="")
#     for o in range (i,i+1):
#         if o>1 and o<5:
#             print(o,end="")
#     print()

##### 48
# A=["A","B","C","D","E"]
# n=len(A)
# for i in range (0,n):
#     for j in range (0,i+1):
#         print(A[j],end="")
#     for k in range (i-1,-1,-1):
#         print(A[k],end="")
#     print()

##### 49
# n=5
# for i in range (1,n+1):
#     for j in range (i,n+1):
#         print("*",end="")
#     for k in range (1,i+1):
#         print(" ",end="")
#     for l in range (1,i+1):
#         print(" ",end="")
#     for m in range (i,n+1):
#         print("*",end="")
#     print()
# n=5
# for i in range (1,n+1):
#     for k in range (1,i+1):
#         print("*",end="")
#     for j in range (i,n+1):
#         print(" ",end="")
#     for m in range (i,n+1):
#         print(" ",end="")
#     for l in range (1,i+1):
#         print("*",end="")
    # print()

##### 50
# n=5
# for i in range (1,n+1):
#     for j in range (1,i+1):
#         print("*",end="")
#     for k in range (n,i,-1):
#         print(" ",end="")
#     for l in range (n,i,-1):
#         print(" ",end="")
#     for m in range (1,i+1):
#         print("*",end="")
#     print()
# n=5
# for i in range(1,n+1):
#     for k in range (n,i,-1):
#         print("*",end="")
#     for j in range (1,i+1):
#         print(" ",end="")
#     for m in range (1,i+1):
#         print(" ",end="")
#     for l in range (n,i,-1):
#         print("*",end="")
#     print()

##### 51
# n=4
# for i in range(1,n+1):
#     for j in range (n+1,i+1,-1):
#         print(" ",end="")
#     for k in range (1,n+1):
#         print("*",end="")
#     print()
#     print()
    
##### 54
# n=4
# for i in range (1,n+1):
#     # print(n)
#     for j in range (n+1,i,-1):
#         print(" ",end="")
#     for k in range (1,n+1):
#         if (i==4):
#             print("*",end="")
#         elif ((i==3 or i==2) and (k==4 or k==1)):
#             print("*",end="")
#         elif (i==1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
#     print()

##### 52
# n=6
# for i in range (1,n+1):
#     for j in range (3,i+1):
#         print(i,end="")
#     print()
# n=5
# for i in range (n,0,-1):
#     for j in range (3,i+1):
#         print(i,end="")
#     print()

##### 53
# n=3
# for i in range (1,n+1):
#     # print(i)
#     for j in range (1,6):
#         print("*",end="")
#     print()
#     print()

##### 55
# n=4
# for i in range (1,n+1):
#     for j in range (1,i+1):
#         print(i,end="")
#         if i>1 and j<i:
#             print("*",end="")
#     print()
# n=4
# for i in range (n,0,-1):
#     for j in range (0,i):
#         print(i,end="")
#         if i>1 and j<i-1:
#             print("*",end="")
#     print()

##### 56
# n=3
# for i in range (1,n+1):
#     for j in range (1,6):
#         if i==2 and j>=2 and j<5:
#             print(" ","",end="")
#         else:
#             print("*","",end="")
#     print()
#     print()

##### 57

##### 58
# n=4
# a=1
# for i in range (1,n+1):
#     for j in range (1,i+1):
#         print(a,end="")
#         if i>1 and j<i:
#             print("*",end="")
#         a=a+1
#     print()

##### 59
# n=5
# for i in range (1,n+1):
#     for j in range (n+1,i+1,-1):
#         print(" ","",end="")
#     for k in range (i,i+1):
#         if k>1:
#             print("*","",end="")
#         else:
#             print(" ","",end="")
#     for k in range (2,i+1):
#         print(" ","",end="")
#     for m in range (i,i+1):
#         print("*","",end="")
#     for o in range (2,i+1):
#         print(" ","",end="")
#     for p in range (i,i+1):
#         if p>1:
#             print("*","",end="")
#     print()
# n=11
# for i in range (1,n+1):
#     print("*","",end="")
# print()
# n=5
# for i in range (1,n+1):
#     for j in range (2,i+1):
#         print(" ","",end="")
#     for k in range (i,i+1):
#         if i<n:
#             print("*","",end="")
#         else:
#             print(" ","",end="")
#     for l in range (n+1,i+1,-1):
#         print(" ","",end="")
#     for m in range (i,i+1):
#         print("*","",end="")
#     for o in range(n+1,i+1,-1):
#         print(" ","",end="")
#     for p in range (i,i+1):
#         if i<n:
#             print("*","",end="")
#     print()

##### 60
# n=5
# for i in range (1,n+1):
#     for j in range (n+1,i+1,-1):
#         print(" ","",end="")
#     for k in range (i,i+1):
#         if k>1:
#             print("*","",end="")
#         else:
#             print(" ","",end="")
#     print()
# n=13
# for i in range (1,n+1):
#     if i>1:
#         print("*",end="")
#     else:
#         print(" ",end="")
# print()
# n=5
# for i in range (1,n+1):
#     for j in range (2,i+1):
#         print(" ","",end="")
#     for k in range (i,i+1):
#         if i<n:
#             print("*","",end="")
#         else:
#             print(" ","",end="")
#     print()