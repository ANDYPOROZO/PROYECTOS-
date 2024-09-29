# Creando un diccionario con información ficticia
informacion_personal = {
    "nombre": "ANDY POROZO",  # Clave: nombre
    "edad": 21,               # Clave: edad
    "ciudad": "Quito",        # Clave: ciudad
    "profesion": "Ingeniero"   # Clave: profesion
}

# Acceder al valor asociado con la clave "ciudad"
print("Ciudad original:", informacion_personal["ciudad"])

# Modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Guayaquil"
print("Ciudad actualizada:", informacion_personal["ciudad"])

# Agregar una nueva clave-valor "telefono" al diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0979577788"  # Teléfono ficticio

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
print("Diccionario final:", informacion_personal)
