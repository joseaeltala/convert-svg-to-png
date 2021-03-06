#!/usr/bin/python3
from cairosvg import svg2png
import os
import sys
import re

try:   
    args = sys.argv[1:]
    file = open(args[0],"rt")
    png_dir = args[1]
    filename = args[2]
    file_content = file.read()
    svg_code = re.findall('.*svg.*',file_content)

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
    for code in svg_code:

        pngf = png_dir + '/' + filename + ".png"

        cn = 1
        while os.path.exists(pngf):
            pngf = png_dir + '/' + filename + '-' + str(cn) + ".png"
            cn+=1

        svg2png(bytestring=code,write_to=pngf)
        file_content = file_content.replace(code,'![](' + pngf + ')')

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
