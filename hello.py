# Ask user for their name
name = input("What's your name? ").strip().title()  # --> all in one line

# Split user's name into first name and last name
first, last = name.split()

print(f"hello, {first}")  # --> formats strings in special way

# Remove whitespaces from str
# name = name.strip()

# Capitalize the user's name --> Only capitalizes first letter of first name and not the last name
# name = name.capitalize()
# name = name.title()

# Say hello to user
# print(
#     "Hello, ", end=""
# )  # --> end is the parameter for which a new line will be added after a string is printed or not
# print(name)


# print("Hello,", name, sep="") # --> sep is the seperator at the start of a new string
# print('Hello, "Friend"') # --> method to include "" in printed text
