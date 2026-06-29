
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