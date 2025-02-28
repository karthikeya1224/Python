import re
email = input('enter email:').strip().lower()
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")
