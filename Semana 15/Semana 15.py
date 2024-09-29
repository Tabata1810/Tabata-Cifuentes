# Creamos un perfil con informacion personal ficticia
informacion_personal = {
    "nombre": "Mateo Naranjo",
    "edad": 23,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Modificamos la clave ciudad
informacion_personal["ciudad"] = "Cuenca"

# Agregamos una nueva clave para profesion
informacion_personal["profesion"] = "Arquitecto"

# Verificamos si la clave telefono existe en el perfil
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0999999999"

# Eliminamos la clave edad
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimos el perfil final usando un bucle for
print("Perfil final:")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")