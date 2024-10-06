# Escritura de Archivo de Texto

# Abrimos el archivo 'my_notes.txt' en modo escritura ('w')
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales en el archivo
    file.write("Primera nota: Aprendiendo a manejar archivos en Python.\n")
    file.write("Segunda nota: El método write() permite escribir en archivos.\n")
    file.write("Tercera nota: Es importante cerrar el archivo después de usarlo.\n")

# Lectura de Archivo de Texto

# Abrimos el archivo 'my_notes.txt' en modo lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Leemos y mostramos cada línea utilizando readline()
    line = file.readline()
    while line:
        print(line.strip())  # El método strip() elimina los saltos de línea al mostrar en consola
        line = file.readline()
