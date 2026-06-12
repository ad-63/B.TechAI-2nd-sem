# greatest among 3 no.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print(f"{a} is the largest.")
elif b >= a and b >= c:
    print(f"{b} is the largest.")
else:
    print(f"{c} is the largest.")                                                                                                                 