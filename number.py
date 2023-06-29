def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


# Note: 'return' is stronger than 'break' as return can break out of the loop and return a value back

main()
