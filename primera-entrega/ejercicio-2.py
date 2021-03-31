import sys
import getopt
import os

(opt, arg) = getopt.getopt(sys.argv[1:], 'i:o:')

print("opciones:", opt)

for (op, ar) in opt:
    if op in '-i':
        file1 = ar
    elif op == '-o':
        file2 = ar
    else:
        print("Opcion invalida")

file = open(file1, "r")
list = file.readlines()
file.close

copytext = open(file2, "w")
for i in list:
    copytext.write(i)
    copytext.close()

print("el archivo se ha copiado correctamente")
