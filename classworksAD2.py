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
class Invalidemail(Exception):
    pass
class  Invalidpassword(Exception):
    pass
valid_email="ad63@gmail.com"
valid_password="adwitiya123"
try:
    email=input("enter your email")
    password=input(" enter your password")
    if email!= valid_email:
        raise Invalidemail("invalid email try again")
    if password!=valid_password:
        raise Invalidpassword(" invalid email")
    print("login successfull")
except Invalidemail as em:
    print(em)
except Invalidpassword as im:
    print(im)

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