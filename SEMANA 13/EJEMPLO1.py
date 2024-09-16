# Datos ficticios de temperaturas en Quito, Guayaquil y Cuenca
temperaturas = [
    [  # Quito
        [  # Semana 1
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 19}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 18}
        ]
    ],
    [  # Guayaquil
        [  # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 33}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 32}
        ]
    ],
    [  # Cuenca
        [  # Semana 1
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 19}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 18}
        ]
    ]
]

# Nombres de las ciudades
ciudades = ["Quito", "Guayaquil", "Cuenca"]


# Función para calcular el promedio de temperaturas
def calcular_promedio_temperaturas(temperaturas, ciudades):
    """
    Función que calcula el promedio de temperaturas por ciudad.

    Parámetros:
    temperaturas: lista de listas con las temperaturas diarias por ciudad y semana.
    ciudades: lista de nombres de las ciudades.

    Retorna:
    Un diccionario con las ciudades y sus promedios de temperatura.
    """
    promedios_por_ciudad = {}  # Diccionario para almacenar los promedios por ciudad

    # Iterar sobre la lista de temperaturas, cada "ciudad" contiene sus semanas y días
    for i, ciudad in enumerate(temperaturas):
        suma_total_temperaturas = 0  # Variable para acumular las temperaturas
        total_dias = 0  # Variable para contar la cantidad de días

        # Iterar sobre cada semana de la ciudad
        for semana in ciudad:
            # Iterar sobre los días de cada semana
            for dia in semana:
                suma_total_temperaturas += dia["temp"]  # Sumar la temperatura del día actual
                total_dias += 1  # Aumentar el contador de días

        # Calcular el promedio total para la ciudad
        promedio_ciudad = suma_total_temperaturas / total_dias
        # Guardar el promedio en el diccionario usando el nombre de la ciudad como clave
        promedios_por_ciudad[ciudades[i]] = promedio_ciudad

    return promedios_por_ciudad  # Retornar el diccionario con los promedios por ciudad


# Llamar a la función para calcular los promedios y mostrarlos
promedios = calcular_promedio_temperaturas(temperaturas, ciudades)

# Mostrar los promedios de temperatura de cada ciudad
for ciudad, promedio in promedios.items():
    print(f"El promedio de temperatura en {ciudad} es: {promedio:.2f}°C")
