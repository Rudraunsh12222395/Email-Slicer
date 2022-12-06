email_list = list(map(str, input("Enter multiple Email: ").split()))
for email in email_list:
    if "@" in email:
        username = email[:email.index("@")]
        domain_name = email[email.index("@")+1:].upper()
        a = (f"Username:{username} Domain:{domain_name}")
        print(a)
    else:
        print("Invalid input type")