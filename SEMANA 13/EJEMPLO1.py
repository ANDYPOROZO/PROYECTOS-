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
    promedios_por_ciudad = {}

    # Iterar sobre la matriz de temperaturas
    for i, ciudad in enumerate(temperaturas):
        suma_total_temperaturas = 0
        total_dias = 0

        # Iterar sobre las semanas
        for semana in ciudad:
            for dia in semana:
                suma_total_temperaturas += dia["temp"]
                total_dias += 1

        # Calcular el promedio total para la ciudad
        promedio_ciudad = suma_total_temperaturas / total_dias
        promedios_por_ciudad[ciudades[i]] = promedio_ciudad

    return promedios_por_ciudad


# Llamar a la función para calcular los promedios y mostrarlos
promedios = calcular_promedio_temperaturas(temperaturas, ciudades)
for ciudad, promedio in promedios.items():
    print(f"El promedio de temperatura en {ciudad} es: {promedio:.2f}°C")
