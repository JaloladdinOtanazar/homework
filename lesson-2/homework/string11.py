string = input("Enter a string: ")
if any(char.isdigit() for char in string):
    print("There are some digits")
else:
    print("There is no digit")