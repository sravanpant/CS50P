import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# username, domain = email.split("@")

# if username and domain.endswith(".com"):
#     print("Valid")
# else:
#     print("Invalid")

# if username and "." in domain:
#     print("Valid")
# else:
#     print("Invalid")

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")
