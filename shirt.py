import sys
from PIL import Image, ImageOps
from os.path import splitext

try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguements")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguements")
    else:
        name1, ext1 = splitext(sys.argv[1])
        name2, ext2 = splitext(sys.argv[2])
        if ext1 == "" or ext2 == "":
            sys.exit("Invalid input")
        elif ext1 != ext2:
            sys.exit("Input and output have different extensions")
        else:
            shirt = Image.open("shirt.png")
            size = shirt.size
            image = Image.open(sys.argv[1])
            before = ImageOps.fit(image, size)
            before.paste(shirt, mask=shirt)
            before.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("File does not exist")
