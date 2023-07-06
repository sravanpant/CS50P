import sys


try:
    count = 0
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguements")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguements")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")
    else:
        with open(sys.argv[1]) as file:
            for line in file:
                if len(line) > 1:
                    if not line.lstrip().startswith("#"):
                        count += 1
            print(count)

except FileNotFoundError:
    sys.exit("File does not exist")
