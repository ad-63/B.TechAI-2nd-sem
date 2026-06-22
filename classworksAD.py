# # wap to show class and objet imlementation
# class student:
# def set_data(self,name,age):
#     self.name=name
#     self.age=age
    
# def display():
#     print(f"name={self.name},age={self.age}")

# std1=student()
# std1.set_data("ram",20)
# std1.display()

#................................................................................................................................................................

# # class and obj

# class student:#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(f"name={self.name},age={self.age}")
#  std1=student("ram",20)
#  std1.display()

#..................................................................................................................................................................

# # to store details of two cars and display the highest priced car.
# class car:
   #  def __init__(self,brand,price):
    


#         self.brand=brand
#         self.price=price

   
#         def display(self):

#          print(f"name={self.name}\n price={self.price}")
         
# c1=car("mercedes",1000000)
# c2=car("hyundai", 800000)
# print(c1.price)
# print(c2.price)
# if c1.print>c2.price:
#    c1.display()
# else:
#    c2.display()

# ..............................................................................................................................................................

# class a:
#     print("xoro yujal k xa  chor aayo")


# class b:
#     print("xori xori yujaliii chorrr aayoooo!!")


# class c(a,b):
#     print("bhag bhag xora xori")


# class book:
    
#     def __init__(self,name,r_year):
#         self.name=name
#         self.r_year=r_year



#     def display(self):

#...............................................................................................................................................................

# wap to input N students detail and display the highest age student details.

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display(self):

#         print(f"Name={self.name}\n Age={self.age}")

# size=int(input("enter how many students to store:"))

# student_list=[]

# for i in range(size):

#     name=input(f"enter{i+1} student name:")
#     age=int(input(f"enter{i+1}student age:"))
#     student_list.append(student(name,age))
# # declearing highest age for comparison    
# highest_age=student_list[0].age
# for std in student_list:
#     if std.age>highest_age:
#         highest_age=std.age
# # printing highest age student details
# for std in student_list:
#     if highest_age==std.age:
#         std.display()
    
# ................................................................................................................................................................

# class ATM:
#     def __init__(self,name,balance):
        
#         self.name=name
#         self.balance=balance
        
#     def update_balance(self):
       
       
#        self.balance=self.balance+5000


#     def display_balance(self):
   
   
   
#       print(f"name={self.name}\n balance={self.balance}")
# atm1=ATM("ram",10000)
# atm1.update_balance() 

#....................................................................................................................................................................  
   
# multiple inheritance: if we inherit the feature and methods from multiple parent class to any one child class then it is called multiple inheritance.

# class father:
#     def land(self):
#         print("land is the property of father")

# class mother:
#     def money(self):
#         print("money is the property of mother")

# class son(father,mother):
#     pass

# son=son()
# son.land()  
# son.money()       

#.................................................................................................................................................................

# class person:
#     def display(self,name):
#         print("name=",name)

# class student(person):
#     pass

# class teacher(person):
#     pass
# std=student()
# std.display("ram")
# teacher=teacher() 
# teacher.display("hari")

#..................................................................................................................................................................

#  polymorphism: it is a feature of oop in which a "methord" have different forms.
# it can be achived in two ways:
# 1. method overloading: when we have more than one method with the same name but different parameters in the same class then it is called method overloading.
# 2. method overriding: when we have a method in the parent class and the same method in the child class then it is called method overriding.

# method overloading:

# class animal:
#      def sound(self):
#          print("animal sound")

# class dog(animal):
#        def sound(self):
#           print("dog barks")

# class cat(animal):
#         def sound(self):
#             print("cat meows")     

# dog=dog()
# dog.sound()
# cat=cat()
# cat.sound()

#...................................................................................................................................................................

# methord overriding finding area example:

# class calculation:
#       def area(self):
#          print("area")

# class rectangle(calculation):
#      def __init__(self,lenth,breadth):
#          self.length=lenth 
#           self.breadth=breadth
#      def area(self):
#           print("area of rectangle=",self.length*self.breadth)

# class circle(calculation):
#      def __init__(self,radius):
#           self.radius=radius
#      def area(self):
#           print("area of circle=",3.14*self.radius*self.radius)
# rect=rectangle(5,3)
# circle=circle(4)
# rect.area()
# circle.area()                            

#...................................................................................................................................................................    

# method overloading:
#  it is a process of creating same name method in a class with different length of parameters.
# -default argument concept is used for method overloading in python.
# -in reality, overloading is not achived in pyrhon like c++ or java.

# class calculation:
#     def sum(self,num1,num2)
#         print("sum=",self.num1+self.num2)

#     def sum(self,num1,num2,num3=0):
#         print("sum=",self.num1+self.num2+self.num3)    

# cal=calculation()
# cal.sum(5,10)
# cal.sum(5,10,15)     

#...................................................................................................................................................................

# encapsulation: a process of binding and methods into a single unit which protects the direct data access is called encapsulation.
# - variables in python are public, protected and private.
# access modifiers:

# (modifiers)                      (symbols)                                         
# -public -protected -private      -variableName -_variableName -__variableName   
   
# # ACCESS
# (same class)                                    (child class)                                     (outside class)
# (public,protected,private)  (yes,yes,yes)      - (no,yes,yes)                                     - (no,no,yes)      

#....................................................................................................................................................................

# class father: 
#      def __init__(self): 
#           self.name="sanjib" 
#           self.__age=21 
#     def set_age(self,age): 
#                self.__age=age 
# father=father()
# father.__age=25
# print(father._father__age)

# class father: 
#      def __init__(self): 
#           self.name="sanjib" 
#           self.__age=21 
#           self.__gender="male"

#     def set_age(self,age): 
#                self.__age=age 
#     def get_age(self):
#         return self.__age
           
# class son(father):
#     def display(self):
#         print(f"name={self.name}\n age={self.__age}\n gender={self.gender}")
# son=son()
# son.display()

#.................................................................................................................................................................

# 1- setter and getter functions:
    # a) stter function is a function which is used to set the values for private variables inside a class.
        # eg: 
# if__age is private variable then:
#     def set_age(self,age):
#             self.__age=age

# b) gtter fucntion are used to acess the private variables values outside the class. since private variables cannot be accuessed outside the cladd, so we use gether function.
# eg:
# if __age is private variable then if we try to access outside class:
# then if we try to acess outside class:
# father=father()
# father.__age ---->error since __age is private variable and cannot be accessed outside the class.
# so, we use getter functions.

#...............................................................................................................................................................

# *features of OOP:
# 1. class and object
# 2. inheritance
# 3. polymorphism
# 4. encapsulation
# 5. data abstraction
 
#................................................................................................................................................................

# data abstraction: it is a process of hiding the internal details from users and showing only the required features or methods.

#eg:
# class car:
#     def __init__(self):
#         print("car starting...") 
#         self.__fuel_check() # calling private method inside the class
#         self.__bettery_check()
#         self.__condition_check()

#     def __fuel_check(self):
#          print("fuel checked...") 
#     def __bettery_check(self):
#          print("bettery checked...")
 
#     def __condition_check(self):
#          print("condition checked...")

#     def drive(self):
#          print("car is driving...")
# car=car()
# car.drive()       
# 
# class Instagram:
#     def login(self, email, password):
#         self.email = email
#         self.password = password
#         if self.__check_email() and self.__check_password():
#             print("Login successful")
#         else:                                         
#             print("Email or password does not match")

#     def __check_email(self):
#         print("Email checking....")
#         if self.email == "ad@gmail.com":
#             return True
#         else:
#             print("Email does not match")
#             return False

#     def __check_password(self):
#         print("Password checking....")
#         if self.password == "12345":
#             return True
#         else:
#             print("Password does not match")
#             return False

# insta = Instagram()
# insta.login("ad@gmail.com", "12345")

#.................................................................................................................................................................

# new style class: it is a feature avilable from python 3 which supports the top level object by default.
# -> in older versions of python such as python 2 we have to inherit object to all classes.
# ->supports mro and super by default.

# class A:
#     def show():
#         print("show A")
# class B:
#     def show():
#         print("show B")
# class C(A,B):
#     pass
# c=C()
# c.show()
          
# .................................................................................................................................................................

# modules: modules are the python files containing variables, functions and class which can be used inside other files.
# -> it is used as reuseable codes in different files.
# eg:

# in student.py 

# class student:
#     def __init__(self,name,age,address):
#         self.name=name
#         self.age=age
#         self.address=address

#     def display(self):
#         print(f"name={self.name}\n age={self.age}\n address={address}")

# in main.py
# # importing files and its related classes from student import student
# std=student("AD", 19,"dai vai ko chiya")
# std.display()

# .........,..................................................................................................................................

# iterator: iterator is an object that allows to access elements of a collection one at a time using next() function. 
# -> the iter() function is used to create iterator from iterable objects like list, tuple and stiring.

# num=[5,2,1,18,20]
# n=iter(num)
# print(next(n))
# print(next(n))   
# print(next(n)) 
# print(next(n))

# num=[5,2,3,4,1]
# n=iter(num)
# while True:
#     try:
#         print(next(n))
#     except StopIteration:
#         print("no more elements in list")
#         break

# generators : generators are special function used to generate one value at a time using yield keyword.

# def display():
#     yield 1
#     yield 2 
#     yield 3
#     yield 4
#     yield 5
# num=display()
# print(next(num))

# # wap to show class and objet imlementation
# class student:
# def set_data(self,name,age):
#     self.name=nameself.age=age
# std1=student()
# std1.set_data("ram",20)

# .................................................................................................................................................

# instance variable: variables associated with any specifc objects are instance variables.
# -> those values created for one object are not avaiable for other bjects.
# eg:
# class student:
#     def __init__(self,name.age):
#         self.age=self.age
#         self.name=name
#     def display(self):
#         print(f"name"={self.name}\n age={self.age})
# std1=student("sunil",19)
# std2=student("rachit",20)
# std1.display()
# std2.display()

#...............................................................................................................................................

#static methods:
# static methods are those methods used as utility functions that does not needs to be called by creating an object rather we can call by its related class name.
# eg:
# class temprature:
#     college_name="orchid"
#     @classmethod
#     def show_college(cls):
#         cls.college_name="golden gate"
# print(temprature.show_college())

# destructor: it is called automatically to destroy the created objects.
# -> we use __del__ method to create a destructor.
# eg:
# class student:
#     def __init__(self,name)
#         self.name=name
#     def display(self):
#         print(f"name={self.name}")
#     def __del__(self):
#         print("deleted object")
# std=student("ram")
# std.display()

#................................................................................................................................

# execptions:
# exceptions are the errors generated during the execution of a program which can be hanlded using by and except.
# --> exception is the base class for most of the system generated errors.
# --> exception handling is a process of handling the errors using pred=defined exception classes ir with custom exceptions.
# eg:
# witout exception handling:
# print("program started")
# print(50/0) #errors
# print("program ended")
# #--> this will crash the whole program due to a single exception "zerodivisionerror".but we want the above and below statements.
# # with exception hanlding.
# print("program started")
# try:
#     print(50/0)
# except:
#     print("zero division error occured")
# print("program ended")
# #--> try:
# code that might generate any exceptions are written inide the try black.
#--> except:
# if any exception that would be generated inside the try block then except block does handles it.

# in diagram:

#BaseException ---> exception ---> zerodivision error - index error - value error - name error - type error - FileNotFound error
# try: 
#     print(50/0)
# except ZeroDivisionError:
#     print("number cannot be divided by zero")
# # nums=[1,5,12,6,18]
# # print(nums[5]
# num=int(input("abc"))
# print(num)


# catching specfic error:
# when we give class name of any exceptions specifically then it secomes catching specific errors.
# eg: 
# withot specific:
# try:
#     //block of Code 
# except: 
#     //block of code 

# with specific:
#     try: 
#         //block of code 
# except valueError:
#        //block of code 


# .....................................................................................................................

# finally:
# finally is a block of code that gets executed for sure whether the programs has exceptions or not.
# --> used for:
      # .closing database connections.
      # .closing files
#         .closing network connecctions

# # syntax:
#       try:
#         //statement
#       except: 
#         //statement
#       finally: 
#         //statement
    