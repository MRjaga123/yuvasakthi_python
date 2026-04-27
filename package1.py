class calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def mod(self):
        return self.a%self.b

def palindrome(n):
    if len(n)<=1:
            return True
    if n[0]!=n[-1]:
            return False
    return palindrome(n[1:-1])

def adam_number(n):
    square_n=pow(n,2)
    square_reverse_n=0
    for i in str(square_n):
        last_digit=square_n%10
        square_reverse_n=square_reverse_n*10+last_digit
        square_n//=10
    n1=n    
    reverse_n=0
    for i in str(n1):
        last_digit=n1%10
        reverse_n=reverse_n*10+last_digit
        n1//=10
    reverse_square_n=pow(reverse_n,2)
    if reverse_square_n == square_reverse_n:
        return f"{reverse_square_n},{square_reverse_n} it is adam number"
    else:
        return "it is not a adam number"

def armstrong(n):
    n=153
    n1=n
    len_n=len(str(n))
    sum=0
    for i in str(n):
        last_digit=n%10
        sum=sum+pow(last_digit,len_n)
        n//=10
    if sum==n1:
        print("Armstrong")
    else:
        print("Not Armstrong")  
        
def power(x,n):
    if n==0:
        return 1
    return x*power(x,n-1)

def square_root(n):
    if n==0 or n==1:
        return n
    start=1
    end=n
    while start<=end:
        mid=(start+end)//2
        if mid*mid==n:
            return mid
        elif mid*mid<n:
            start=mid+1
            ans=mid
        else:
            end=mid-1
    return ans

def max(a):
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i]<a[j]:
                a[i],a[j]=a[j],a[i]
    return a[0]
def min(a):
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a[0]


