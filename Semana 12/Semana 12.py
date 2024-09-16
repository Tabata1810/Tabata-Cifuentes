# Definimos la matriz 3D con datos de temperaturas
print("Promedio de temperaturas de 3 ciudades durante 3 semanas")
print("")
# Suponemos 3 ciudades, 7 ndías (de lunes a domingo) y 3 semanas
temperaturas = [
    # Manta
    [
        [20, 21, 19],  # Lunes, semana 1, semana 2 y semana 3
        [21, 22, 23],  # Martes
        [19, 20, 22],  # Miércoles
        [22, 23, 18],  # Jueves
        [20, 19, 24],  # Viernes
        [23, 22, 20],  # Sábado
        [24, 23, 21]  # Domingo
    ],
    # Guayaquil
    [
        [25, 26, 25],  # Lunes
        [24, 25, 27],  # Martes
        [26, 27, 24],  # Miércoles
        [27, 26, 26],  # Jueves
        [25, 24, 27],  # Viernes
        [28, 27, 26],  # Sábado
        [26, 25, 28]  # Domingo
    ],
    # Ibarra
    [
        [15, 16, 16],  # Lunes
        [16, 17, 20],  # Martes
        [21, 18, 18],  # Miércoles
        [17, 18, 15],  # Jueves
        [17, 16, 17],  # Viernes
        [18, 17, 19],  # Sábado
        [19, 18, 21]  # Domingo
    ]
]

# Ciudades y semanas
ciudades = ["Manta", "Guayaquil", "Ibarra"]
semanas = ["Primera Semana", "Segunda Semana", "Tercera Semana"]

# Cálculo del promedio
for ciudad in range(len(temperaturas)):
    print(f"Promedio de temperaturas para {ciudades[ciudad]}:")

    for semana in range(len(semanas)):
        suma_temperaturas = 0
        for dia in range(len(temperaturas[ciudad])):
            suma_temperaturas += temperaturas[ciudad][dia][semana]

        promedio = suma_temperaturas / len(temperaturas[ciudad])
        print(f"  {semanas[semana]}: {promedio:.2f}°C")