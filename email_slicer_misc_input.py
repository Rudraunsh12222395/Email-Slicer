import re
my_str = input()
emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", my_str)
user_name = []
domains_name = []
for email in emails:
    user_name.append(email[:email.index("@")])
    domains_name.append(email[email.index("@")+1:])
print(f"Usernames are {user_name} and Domain names are {domains_name}")