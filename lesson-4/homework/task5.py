password = input("Enter a password: ")

if len(password) < 8:
    print("Password is too short.")
else:
    upper_case = False
    for char in password:
        if char.isupper():
            upper_case = True
            break  

    if not upper_case:
        print("Password must contain an uppercase letter.")
    else:
        print("Password is strong.")