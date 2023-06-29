from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

fonts = figlet.getFonts()


if len(sys.argv) != 3:
    f = random.choice(fonts)
elif len(sys.argv) == 3:
    for font in fonts:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] == font:
            f = sys.argv[2]
        # elif sys.argv[1] != "-f" or sys.argv[1] != "-font" or sys.argv[2] != fonts:
        else:
            sys.exit("Invalid usage")

text = input("Input: ")

figlet.setFont(font=f)

print(figlet.renderText(text))
