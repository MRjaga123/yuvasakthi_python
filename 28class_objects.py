# class and object

# 1.without arguments and without return type
class addition():
    def sum(self):
        self.a=int(input("enter a:"))
        self.b=int(input("enter b:"))
        self.c=self.a+self.b
        print(f"sum={self.c}")
ad=addition()
ad.sum()

# 2.with arguments and without return type
class addition():
    def sum(self,a,b):
        self.c=a+b
        print(f"sum={self.c}")
ad=addition()
ad.sum(4,4)

# 3.with arguments and with return type
class addition():
    def sum(self,a,b):
        self.c=a+b
        return self.c
ad=addition()
print(ad.sum(4,4))

# 4.without arguments and with return type
class addition():
    def sum(self):
        self.a=int(input("enter a:"))
        self.b=int(input("enter b:"))
        self.c=self.a+self.b
        return self.c
ad=addition()
print(ad.sum())

#####constructor
class addition():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        self.c=self.a+self.b
        return self.c
ad=addition(4,4)
print(ad.sum())

# #####__name__=="__main__"

##### inheritance
# 1.single inheritance
# 2.multi level inheritance
# 3.hierarchical inheritance
# 4.multiple inheritance
# 5.hybrid inheritance

# single inheritance
class parent():
    def display(self):
        print("this is parent class")
class child(parent):
    def display1(self):
        print("this is child class")
c=child()
c.display() 
c.display1()

# multi level inheritance
class parent():
    def display(self):
        print("this is parent class")
class child(parent):
    def display1(self):
        print("this is child class")
class grandchild(child):
    def display2(self):
        print("this is grand child class")
gc=grandchild() 
gc.display()
gc.display1()
gc.display2()

# hierarchical inheritance
class parent():
    def display(self):
        print("this is parent class")
class child1(parent):
    def display1(self):
        print("this is child1 class")
class child2(parent):
    def display2(self):
        print("this is child2 class")
c1=child1()
c2=child2() 
c1.display()
c1.display1()
c2.display()
c2.display2()

# multiple inheritance
class parent1():
    def display(self):
        print("this is parent1 class")
class parent2():
    def display1(self):
        print("this is parent2 class")
class child(parent1,parent2):
    def display2(self):
        print("this is child class")
c=child()
c.display()
c.display1()
c.display2()

# hybrid inheritance
class parent1():
    def display(self):
        print("this is parent1 class")
class parent2():
    def display1(self):
        print("this is parent2 class")  
class child1(parent1,parent2):
    def display2(self):
        print("this is child1 class")
class child2(child1):
    def display3(self):
        print("this is child2 class")   
c=child2()
c.display()
c.display1()
c.display2()
c.display3()
