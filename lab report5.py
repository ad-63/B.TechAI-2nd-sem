# to find the frequency of the character in name

name = input("Enter your full name: ")
char = input("Enter a character to search: ")
count = name.lower().count(char.lower())
print(f"The character '{char}' appears {count} times.")