# Matriz 3D que representa las temperaturas diarias
# Primera dimensión: Ciudades (Quito, Guayaquil, Cuenca)
# Segunda dimensión: Semanas (2 semanas)
# Tercera dimensión: Días de la semana (7 días)

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

# Iterar sobre la matriz y calcular los promedios de temperatura
for i, ciudad in enumerate(temperaturas):
    print(f"\nTemperaturas para {ciudades[i]}:")

    for j, semana in enumerate(ciudad):
        suma_temperaturas = 0

        print(f"  Semana {j + 1}:")
        for dia in semana:
            print(f"    {dia['day']}: {dia['temp']}°C")
            suma_temperaturas += dia['temp']

        # Calcular el promedio de la semana
        promedio = suma_temperaturas / len(semana)
        print(f"  Promedio de la semana {j + 1}: {promedio:.2f}°C")
