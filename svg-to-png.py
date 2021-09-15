#!/usr/bin/python3
from cairosvg import svg2png
from pathlib import Path
import os
import sys
import re



try:   
    png_dir = "Draws/png/"
    args = sys.argv[1:]
    file = open(args[0],"rt")
    file_content = file.read()
    svg_code = re.findall('.*svg.*',file_content)

    svg_infile = re.search('.*<svg>.*</svg>.*',file_content)
except IndexError:
    print("Falta el primer argumento. Escribe el nombre de un fichero")
    exit
except FileNotFoundError:
    print("Fichero no encontrado.")
    exit
except:
    print("Ha ocurrido algo inesperado")
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
    print("Falla algo en tu código SVG. Puede ser que no esté definido el tamaño.")
    exit
except:
    print("Ha ocurrido algo inesperado")
    exit
else:

    file.close()
    file = open(args[0],"wt")
    file.write(file_content)
    file.close()