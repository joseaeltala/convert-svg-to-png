#!/usr/bin/python3
from cairosvg import svg2png
import os
import sys
import re

try:   
    png_dir = "Draws/"
    args = sys.argv[1:]
    file = open(args[0],"rt")
    file_content = file.read()
    svg_code = re.findall('.*svg.*',file_content)

    svg_infile = re.search('.*<svg>.*</svg>.*',file_content)
except IndexError:
    print("The first argument is missing. Write the name of a file")
    exit
except FileNotFoundError:
    print("File not found.")
    exit
except:
    print("Something unexpected happened")
    exit
else:
    if not os.path.exists(png_dir):
        os.makedirs(png_dir)

try:
    n = 0
    for valor in svg_code:
        n+= 1
        pngf = png_dir + "draw-" + (str(n)) + ".png"
        svg2png(bytestring=valor,write_to=pngf)
        file_content = file_content.replace(valor,'![](' + pngf + ')')

except ValueError:
    print("Something is wrong in your SVG code. The size may not be defined.")
    exit
except:
    print("Something unexpected happened")
    exit
else:

    file.close()
    file = open(args[0],"wt")
    file.write(file_content)
    file.close()
