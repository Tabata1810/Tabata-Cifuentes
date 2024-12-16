# 1. Crear y escribir en el archivo
with open('my_notes.txt', 'w') as file:
    file.write('Jugar básquet es mi pasión.\n')
    file.write('Me gusta leer un libro nuevo cada mes.\n')
    file.write('Amo las películas de terror.\n')
    file.write('Me agrada salir a conocer pueblitos.\n')

# 2. Leemos el contenido línea por línea
with open('my_notes.txt', 'r') as file:
    lines = file.readlines()

# 3. Mostramos cada línea
for line in lines:
    print(line.strip())

# 4. No es necesario cerrar el archivo manualmente, ya que 'with' se encarga de ello automáticamente.