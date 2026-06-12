# to count a digits in a number

num = input("Enter a number: ")
print(f"Number of digits: {len(num.replace('-', '').replace('.', ''))}")