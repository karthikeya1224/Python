import re
str1 = input("Introduce yourself: ").strip()
str2 = input("Do you want to change it? (yes/no): ").strip().lower()

if str2 == "yes":
    pattern = input("Enter the text you want to replace: ")
    replacement = input("Enter the replacement value: ")
    new_intro = re.sub(pattern, replacement, str1)   
    print("Updated introduction:", new_intro)
else:
    print("Your final introduction:", str1)

