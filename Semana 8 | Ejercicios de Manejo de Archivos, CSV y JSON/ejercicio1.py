# Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def open_file_per_line(path1, path2):
    with open(path1, 'r') as file1:
        canciones = file1.readlines()
    canciones.sort()
    with open(path2, 'w') as file2:
        file2.writelines(canciones)

open_file_per_line('/Users/juanmiguel.badilla/Documents/test.txt', '/Users/juanmiguel.badilla/Documents/test2.txt')