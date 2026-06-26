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

#...................................................................................................................
# error:
# error is a problem in a code that stops the further execution of the program crashing the whole program.

#raise keyword: 
# not every kind of errors can be handled by the pythons bilt-in execption classes so the programmers/ developers create their own customised execeptions. then inorder to throw an exception we use raise keyword.

#symtax:
#   raise execption_Name()

#......................................................................................................................

# built in exception classes:
# --> hijako diagram.

# customized exceptions: 
# those exceptions that cannot be handled by thr pythons built in exception classes and we create our own exceptions are called customised exceptions.

# balance = 5000
# withdram_out=int(input("enter a salary"))
# if withdraw_out>balance:
#     raise Exception("ffgg")
# print("withdraw sucessful")

# eg:
# class insufficientBalanceError(exception):

#     pass
# balance=5000
# try:
#     withdraw_balance=int(input("enter amount to withdraw"))
#     if withdraw_balance>balance:

#         rasie insufficientBalanceError("insufficient balance")
#     print("withdraw successful")
# except insufficientBalanceError as e:
#     print(e)

# .....................................................................................................................

#wap to make the  instragram login system draw exception if email or password is invalid 
#email=ashim
# class Invalidemail(Exception):
#     pass
# class  Invalidpassword(Exception):
#     pass
# valid_email="ad63@gmail.com"
# valid_password="adwitiya123"
# try:
#     email=input("enter your email")
#     password=input(" enter your password")
#     if email!= valid_email:
#         raise Invalidemail("invalid email try again")
#     if password!=valid_password:
#         raise Invalidpassword(" invalid email")
#     print("login successfull")
# except Invalidemail as em:
#     print(em)
# except Invalidpassword as im:
#     print(im)

#.....................................................................................................................

# class InvalidAcctNumError(Exception):
#     def __init__(self, acct_num):
#         print(f"Invalid account number: {acct_num}")

# class InvalidPinError(Exception):
#     def __init__(self):
#         print("Invalid PIN")

# class InsufficientBalanceError(Exception):
#     def __init__(self):
#         print("Insufficient balance")

# class BankAccount:
#     def __init__(self):
#         self.acct_num = "00123"
#         self.pin = "1234"
#         self.balance = 100000

#     def withdraw(self):
#         acct = input("Enter your account number: ")
#         input_pin = input("Enter your PIN: ")
#         withdraw_bal = int(input("Enter amount to withdraw: "))
#         if acct != self.acct_num:
#             raise InvalidAcctNumError(self.acct_num)
#         if input_pin != self.pin:
#             raise InvalidPinError()
#         if withdraw_bal > self.balance:
#             raise InsufficientBalanceError()
#         self.balance -= withdraw_bal
#         print("Withdrawal successful")
#         print("Remaining balance =", self.balance)

# try:
#     account = BankAccount()
#     account.withdraw()
# except InvalidAcctNumError as e:
#     print(e)
# except InvalidPinError as e:
#     print(e)
# except InsufficientBalanceError as e:
#     print(e)

#......................................................................................................................

# file handling:
# --> files are  the collection f data which stores data in the centralized storage(disk).
# --> since, data in file are stored in disks, thats why we can fetch data even after years in time and are avaliable till we destroy them.
# --> file handling is a process of reading from and writing to a file.

# step in file handling:
# i) opening a file --> open() function is used
# ii) reading or writing to a file --> write() or read() function is used
# ii) closing the file --> close() function is used

# files can be accessed in two ways
# a) sequential access: 
#                --> follos a sequential pattern one after another.
# eg: 1-->2-->3-->4.  time complexity=0(n)

#b) random access: we can fetch data from where we went i.e no any sequential order.
# eg: if we want to fetch from 5th index, we can directly fetch it.
#"python programming" 
# from 5th --> N programming.  --> time complexity-->0(i)

# modes in file handling:
# a) w----> wite mode
# b) r----> read mmode
# c) a----> append mode
# d) wt---> write + read
# e) rt---> read + write
# f) x----> execute 
# g) xt---> execute + read or write
# h) at---> append + read

# 1) WAP to store "purbanchal university"in py.txt
# syntax: --> open(filename, mode)   --> write(w) mode --> creates a new file if it does not exists previously.
# file=open("pu.txt", "r")
# data=file.read()
# print(data)
# file.close()

# 2) wap to input and write your name into name.txt.

# file=open("name.txt","w")
# name=input("enter your name")
# file.write(name)
# file.close()

#............................................................................................................................

# wap to copy the contents of pu.txt to new_pu.txt.

# file=open("pu.txt","r")
# data=file.road()
# file.close()
# new_file=open("new_pu.txt","w")
# new_file.write(data)
# new_file.close()
# print("data copied successfully")
# new_file=open("new_pu.txt","r")
# new_file_data=new_file.read()
# print(new_file_data)
# new_file.close()

# # wap to inout name, age and address of a student and store it in std.txt.

# file=open("std.txt","w")
# name=input("enter name:")
# age=input("enter age:")
# address=input("enter address")
# file.write(f"{name}\n{age}\n{address}")
# print("Data stored successfully")
# file.close()

# # wap to cunt no. of vowels in a file std.txt

# file=open("std.txt","r")
# count=0
# data=file.read()
# for ch in data: 
#     if ch in "aeiou":
#         count=count+1
# print("number of vowels=", count)

# wap to input name for 5 students and store it in many_std.txt file

# file=open("std.txt","w")
# print("enter the names of 5 students:")

# for i in range(1, 6):
#     name = input(f"Enter name for student {i}: ")
#     file.write(name + '\n')

# file.close()

# print("\nSuccessfully saved the names to many_std.txt.")

#.........................................................................................................................

# WAP to input name, age, address of N number of students nand diplay the youngest age student detail.

n = int(input("Enter the number of students: "))
students = []
for i in range(n):
    print(f"\nEnter details for student {i + 1}:")
    name = input("Name: ")
    age = int(input("Age: "))
    address = input("Address: ")
    students.append({
        "name": name,
        "age": age,
        "address": address
youngest_student = min(students, key=lambda s: s["age"])


print("\n--- Youngest Student Details ---")
print(f"Name: {youngest_student['name']}")
print(f"Age: {youngest_student['age']}")
print(f"Address: {youngest_student['address']}")

# 2) WAP to read a gile std.txt and store all vowels into vowels.txt and all consonants into condonents.txt.

vowels_list = 'aeiouAEIOU'

try:
    with open("std.txt", "r") as source_file, \
         open("vowels.txt", "w") as vowel_file, \
         open("consonants.txt", "w") as consonant_file:
        content = source_file.read()
        
        for char in content:
            if char.isalpha():
                if char in vowels_list:
                    vowel_file.write(char)
                else:
                    consonant_file.write(char)
                    
    print("File processing completed successfully.")

except FileNotFoundError:
    print("Error: The file std.txt was not found. Please create it first.")

#................................................................................................................................

# wap to read only 3 names frm a file std_name.txt

file=open("std_name.txt","r")
count=0
for i in range(3):
    data=file.readline()
    print(data.strip())
print("data fecthed sucessfully.")

#.........................................................................................................................

