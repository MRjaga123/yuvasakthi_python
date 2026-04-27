#rectangle
l=int(input("enter l: "))
b=int(input("enter b: "))
A=l*b #area
P=2*(l+b) #perimeter
print("a:",A,"b:",P)

#square
a=int(input("enter: "))
A=pow(a,2) #area
P=4*a #perimeter
print("A:",A,"P:",P)

#parelogram 
l=int(input("enter: "))
h=int(input("enter: "))
b=int(input("enter: "))
A=l*h #area
P=2*(l+b) #perimeter
print("A:",A,"P:",P)

#triangle
s=int(input("enter: "))
a=int(input("enter: "))
b=int(input("enter: "))
c=int(input("enter: "))
import math
A=math.sqrt(s*((s-a)*(s-b)*(s-c))) #area
S=(a+b+c)/2 #perimeter
print("A:",A,"S:",S)

#right angle triangle
b=int(input("enter: "))
h=int(input("enter: "))
d=int(input("enter: "))
A=1/2*(b*h) #area
P=b+h+d #perimeter
print("A:",A,"P:",P)

#equilateral triangle
a=int(input("enter: "))
A=math.sqrt(3)*pow(a,2)/4 #area
P=3*a #perimeter
print("A",A,"p",P)

#isoceles triangle 
a=int(input("enter: "))
d=int(input("enter: "))
A=1/2*(pow(a,2)) #area
P=(2*a*d)+d #perimeter
print("A",A,"P",P)

#trapezium
h=int(input("enter: "))
a=int(input("enter: "))
b=int(input("enter: "))
A=(1/2*h)*(a+b) #area
print("A:",A)

#rhombus
d1=int(input("enter: "))
d2=int(input("enter: "))
l=int(input("enter: "))
A=1/2*(d1*d2)
P=4*l
print("A:",A,"P:",P)

#quadrilateral
a=int(input("enter: "))
b=int(input("enter: "))
c=int(input("enter: "))
d=int(input("enter: "))
P=(a*b)+(b*c)+(c*d)+(d*a)
print("p:",P)

#circle
r=int(input("enter: "))
A=math.pi*(pow(r,2))
P=2*math.pi*r
print("A:",A,"P:",P)

#frustum
h=int(input("enter: "))
r1=int(input("enter: "))
r2=int(input("enter: "))
A1=math.pi*h*(r1+r2)
A2=math.pi*(pow(r1,2)+h*(r1+r2)+pow(r2,2))
print("A1:",A1,"A2:",A2)

#cube
a=int(input("enter: "))
side=int(input("enter: "))
l=int(input("enter: "))
A=4*a
P=12*(side)
V=pow(l,3)
D=math.sqrt(3)*l
print(A,P,V,D)

#cuboid
l=int(input("enter: "))
b=int(input("enter: "))
h=int(input("enter: "))
A=6*pow(l,2)
P=4*(l+b+h)
V=l*b*h
D=math.sqrt(pow(l,2)+pow(b,2)+pow(h,2))
print(A,P,V,D)

#right circular cylinder
h=int(input("enter: "))
R=int(input("enter: "))
r=int(input("enter: "))
A1=2*(math.pi*(r*h))
A2=2*math.pi*h*(pow(R,1)-pow(r,2))
V1=math.pi*pow(r,2)*h
V2=math.pi*h*(pow(R,2)-pow(r,2))
print(A1,A2,V1,V2)

#right circular cone 
r=int(input("enter: "))
l=int(input("enter: "))
h=int(input("enter: "))
A1=math.pi*(r*l)
A2=math.pi*r*(r-l)
V=1/3*math.pi*pow(r,2)*h
print(A1,A2,V)

#sphere
r=int(input("enter: "))
S=4*math.pi*pow(r,2)
V=4/3*math.pi*pow(r,3)
print(S,V)

#hemisphere
r=int(input("enter: "))
A1=2*math.pi*pow(r,2)
A2=3*math.pi*pow(r,2)
V=2/3*math.pi*pow(r,3)
print(A1,A2,V)

#tetrahedron
a=int(input("enter: "))
A1=3*pow(a,2)*(math.sqrt(3)/4)
A2=math.sqrt(3)*pow(a,2)
V=(math.sqrt(2)/12)*a
print(A1,A2,V)

#regular hexagon 
a=int(input("enter: "))
A=3*math.sqrt(3)*pow(a,3)/2
P=6*a
print(A,P)
