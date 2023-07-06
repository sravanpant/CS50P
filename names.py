names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())


for name in sorted(names, reverse=True):
    print(f"hello, {name}")

# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())

# not very elegant
# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print(f"hello,", line, end="")

# name = input("What's your name? ")

# to not close the file again and again and keep the code clean
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")
# after line 5 the file will be automatically closed

# file = open("names.txt", "w") # --> w recreates the file and replace the old content with new one
# file = open("names.txt", "a")  # --> a means append which adds content to the bottom
# file.write(f"{name}\n")
# file.close() # --> need to manually close the file again and again


# names = []

# for _ in range(3):
#     names.append(input("What's your name? "))

# for name in sorted(names):
#     print(f"hello, {name}")

# name = input("What's your name? ")
# print(f"hello, {name}")
