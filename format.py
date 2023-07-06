import re

name = input("What's your name? ").strip()

if matches := re.search("^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

# if matches:
#     name = matches.group(2) + " " + matches.group(1)
# print(f"hello, {name}")

# if matches:
#     last, first = matches.group()
#     name = f"{first} {last}"
# print(f"hello, {name}")

# name = input("What's your name? ").strip()
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
# print(f"hello, {name}")
