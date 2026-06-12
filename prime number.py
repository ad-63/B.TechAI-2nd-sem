# to check if it is prime or not.

num=int(input("enter a number:"))
count=0
for i in range(2,5):
    if num%i==0:
        count+=1
        break
if count==0:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")