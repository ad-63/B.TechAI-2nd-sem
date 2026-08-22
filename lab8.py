# import re

# phone = input("Enter phone number: ")
# pattern = r"^(98|97)\d{8}$"

# if re.match(pattern, phone):
#     print("Valid phone number.")
# else:
#     print("Invalid phone number.")


#......................................................


# import re

# email = input("Enter email address: ")
# pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# if re.match(pattern, email):
#     print("Valid email address.")
# else:
#     print("Invalid email address.")




#......................................................



# import re

# password = input("Enter password: ")
# pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,16}$"

# if re.match(pattern, password):
#     print("Strong password.")
# else:
#     print("Weak password.")


#.......................................................




# import threading
# import time

# months = ["January", "February", "March", "April", "May", "June",
#           "July", "August", "September", "October", "November", "December"]

# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# def show_months():
#     for m in months:
#         print(m)
#         time.sleep(1)

# def show_days():
#     for d in days:
#         print(d)
#         time.sleep(1.5)

# t1 = threading.Thread(target=show_months)
# t2 = threading.Thread(target=show_days)

# t1.start()
# t2.start()

# t1.join()
# t2.join()



#.......................................................




import threading

def natural_numbers():
    for i in range(1, 11):
        print(f"Natural: {i}")

def even_numbers():
    for i in range(2, 21, 2):
        print(f"Even: {i}")

def odd_numbers():
    for i in range(1, 20, 2):
        print(f"Odd: {i}")

t1 = threading.Thread(target=natural_numbers)
t2 = threading.Thread(target=even_numbers)
t3 = threading.Thread(target=odd_numbers)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()