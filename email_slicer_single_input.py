email = input("Enter your email:").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:].upper()
a = (f"Username:{username} Domain:{domain_name}")
if "@" in email:
    print(a)
else:
    print("Invalid input type")    
