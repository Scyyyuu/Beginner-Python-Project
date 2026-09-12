password = input("Enter your password: ")
length_ok = len(password) >= 8

has_digit = False
has_upper = False
has_symbol = False
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"

for letter in password:
    if letter.isdigit():
        has_digit = True
    if letter.isupper():
        has_upper = True
    if letter in symbols:
        has_symbol = True

if not length_ok:
    print(f"Weak — password must be at least 8 characters (yours has {len(password)})")

elif has_digit and has_upper and has_symbol:
    print("Strong password")

else:
    if not has_upper and has_digit and has_symbol:
        print (f"Medium - password must contain uppercase letter")
    elif not has_digit and has_upper and has_symbol:
        print (f"Medium - password must contain digit number")
    elif not has_symbol and has_upper and has_digit:
        print (f"Meidum - password must contain a symbol")
    elif not has_symbol and not has_upper and has_digit:
        print (f"Medium - password must contain both uppercase letter and symbol")
    elif not has_symbol and not has_digit and has_upper:
        print (f"Medium - password must contain both digit number and symbol")
    elif not has_upper and not has_digit and has_symbol:
        print (f"Medium - password must contain both uppercase letter and digit number")
    elif not has_digit and not has_upper and not has_symbol:
        print (f"Medium - password must contain an uppercase letter, digit number, and symbol")
    