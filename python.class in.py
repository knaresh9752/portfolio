#Inhertiance:Inheritance means one class (child class) can use the properties & methods of another class (parent class).
#single:
#multilevel:
#multiple:
#hierarical
#hybrid
'''class shape:
    def perimeter(self):
        print("perimeter")
    def area(self):
        print("Area")
class Rectangle(shape):
    pass
rectangle=Rectangle()
rectangle.area()
rectangle.perimeter()'''
#single:oneparent,singlechild
'''
    def bike(self):
        print("Hero cycle")
object=child()
#object.bike()
#object.car()
#object.acre1()
f_object=parent()
f_object.acre1()
f_object.bike() #parent' object has no attribute 'bike' '''
'''class grandparent():
    def home(self):
        print("Home")
    def Bicycle(self):
        print("Hero cycle")
class parent():
    def acre1(self):
        print("Acre-1")
    def acre2(self):
        print("Acre-2")
    def acre3(self):
        print("Acre-3")
class child(parent):
    def car(self):
        print("mercedes")
    def book(self):
        print("book")
    def Bicycle():
        print("Bicycle")
object=child()
#object.car()
#object.acre1()
object.book()
#object.Bicycle()
f_object=parent()
f_object.acre1()
#f_object.bike() '''
'''
class mother():
    def acre1(self):
        print("Acre-1")
    def acre2(self):
        print("Acre-2")
    def acre3(self):
        print("Acre-3")
class father(mother):
    def home(self):
        print("Home")
    def car(self):
        print("car")
class child(father):
    def car(self):
        print("mercedes")
    def book(self):
        print("book")
    def Bicycle():
        print("Bicycle")
object=father()
object.car()'''
'''print(len("rajesh"))
print(len([1,2,3,4]))'''
'''
def add(a:int,b:int):
    print(a+b)
def add(c:int,d:int):
    print(c*10)
a=10
b=20
add(a,b)'''
'''
class shape:
    def area(self):
        print("sample area is 0")
    def perimeter(self):
        print("sample area is 10")
class Rectangle(shape):
    def area(self):
        print("area of 10sqm")
r1=Rectangle()
r1.area()
r1.perimeter()'''
'''
def add (a:int,b:int):
    print(a+b)
def add (c:int,d:int):
    print(c*d)
a=10
b=30
add(a,b)'''
'''
from multimethod import multimethod
@multimethod
def add(a:int,b:int):
    print(a+b)
@multimethod
def add(c:int,d:int):
    print(c*10)
a=10
b=20
add(a,b)
'''
'''
from multipledispatch import dispatch
@dispatch(int,int,int)
def add(a,b,c):
    print(a+b+c)
@dispatch(int,int)
def add(a,b):
    print(a+b)
@dispatch(int,)
def add(c):
    print(c*10)
#a=20
#b=30
c=30
#add(a,b,)
add(c)'''
'''
from multimethod import multimethod
@multimethod
class shape:
    def area(self):
        print("sample area is 0")
    def perimeter(self):
        print("sample area is 10")
class Rectangle(shape):
@multimethod
def area(self,length,int):
    print("area is 10sqm")
@multimethod
def area(self,length:int,width:int):
    print("area is 20sqm")
@multimethod
def area(self):
    super()
r1=Rectangle()
r1.area()
'''
'''
class states():
    def city(self):
        print("self-->",self)
        print("bengaluru")
        self.a=10
My_address=states()
print("My_address-->","address")
My_address.city()
'''
'''
class states():
    def city(self):
        self.name='hyd'
        print(self.name)
address.city()
print(address.name)
address.name="bengalor"
print(address.name)
'''
'''
class states():
    def class(self):
       self.name="hyd"
        print(self.name)
    def class(self)
         print(self.name)
        self.city()
My_address=states()
My_address.city()
My_address.Town()
'''
'''
class Reportcard():
    def __int__ (self):
     self.sub1=0
     self.sub2=0
     self.sub3=0
     self.Total=0
     self.percentage=0 
    def Mymarks(self,sub1,sub2,sub3):
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
    def Totalmarks(self):
        self.Total=self.sub1+self.sub2+self.sub3
        return self.Total
    def percentage(self):
        self.percentage=(self.Total//300)*100
        return self.percentage
    def GradeAchieved(self):
        if 100>self.percentage>90:
            return "A-grade"
        return "B-grade"
Suresh_Reportcard=Reportcard()
#print(Suresh_Reportcard.Mymarks(80,89,90))
#print(Suresh_Reportcard.Totalmarks())
#print(Suresh_Reportcard.percentage(),'%',sep='')
#print(Suresh_Reportcard.GradeAchieved())'''
'''
class marks():
    def __init__(self):
        self.sub1=0
        self.sub2=0
        self.sub3=0
    def members(self,sub1,sub2,sub3):
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
    def Totalmarks(self):
        Total =self.sub1+self.sub2+self.sub3
        return Total
    def Avgmarks(self):
        Total=self.Totalmarks()
        Avg=(Total/300)*100
        return Avg
        
object=marks()
object.members(80,89,90)
print(object.Totalmarks())
print(object.Avgmarks())
'''
'''
class marks():
    def __init__(self):
        self.num11=0
        self.num2=0
        self.num3=0
    def members(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
    def Totalmarks(self):
        Total =self.num1+self.num2+self.num3
        return Total
    def Avgmarks(self):
        Total=self.Totalmarks()
        Avg=(Total/150)*100
        return Avg
        
object = marks()
object.members(40,50,60)
print(object.Totalmarks())
print(object.Avgmarks())'''
'''
class student:
    def __init__(self):
        self.mark1=0
        self.mark2=0
        self.mark3=0
    def my_student(self, roll, name):
        self.roll= roll
        self.name=name
    def marks(self,marks1,marks2,marks3):
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
    def mark(self,marks4,marks5,marks6):
        self.marks4=marks4
        self.marks5=marks5
        self.marks6=marks6
    def Total(self):
        return self.marks1 + self.marks2 + self.marks3
object = student()
o1=student()
object.my_student("1","Hima Shakar Reddy")
o1.my_student("2","hussian")
object.marks(80,89,90)
o1.marks(70,80,90)
print(object.roll)
print(o1.roll)
print(object.name)
print(o1.name)
print(object.Total())'''
'''
class circle():
    def __init__(self):
        self.radius=0
        self.setRadio=0
        self.area=0
        self.circum=0
    def Radius(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def circum(self):
        return 2* 3.14 * self.radius
object=circle()
object.radius
print(object.area)
print(object.circum)'''
class Results():
    