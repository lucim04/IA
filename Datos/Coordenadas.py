from math import radians, sin, cos, sqrt, atan2
from haversine import haversine
"""
Primero usamos Google maps para buscar las coordenadas de cada parada de metro
"""
LISTA_COORDENADAS = {
    "LINEA_A": {
        "Alberti": [-34.60979154021843, -58.40086740463643],
        "Pasco": [-34.609455989895245, -58.39833539938651],
        "Congreso": [-34.608996813572965, -58.39268130286541],
        "Sáenz Peña": [-34.609350026351635, -58.38669461230903],
        "Lima": [-34.60904096524644, -58.382553281561165],
        "Piedras": [-34.60886435838594, -58.37861579874318],
        "Perú": [-34.60857295624564, -58.37492507907565],
        "Plaza de Mayo": [-34.60875839408815, -58.37151330936176],
    },
    "LINEA_B": {
        "Pasteur": [-34.60409382222638, -58.39968610352264],
        "Callao_B": [-34.60434108592872, -58.39243341083207],
        "Uruguay": [-34.60400961150244, -58.38674150304544],
        "Carlos Pellegrini": [-34.60370936151744, -58.381380708823514],
        "Florida": [-34.603244782294965, -58.37454489610343],
        "Leandro N. Alem": [-34.60302925135683, -58.37004749037363],
    },
    "LINEA_C": {
        "Constitución": [-34.62753942668646, -58.38156121435256],
        "San Juan": [-34.622153370728164, -58.37994066311232],
        "Independencia_C": [-34.6180519466846, -58.380256098860485],
        "Moreno": [-34.61237244698663, -58.38060876062811],
        "Avenida de Mayo": [-34.60899098423044, -58.38066790483753],
        "Diagonal Norte": [-34.60482400192541, -58.379488963667214],
        "Lavalle": [-34.60207510706261, -58.37814441867528],
        "General San Martin": [-34.59553840845914, -58.37745834587982],
        "Retiro": [-34.59238671801715, -58.37594819705223],
    },
    "LINEA_D": {
        "Facultad de Medicina": [-34.5993682836706, -58.3977359491304],
        "Callao_D": [-34.59957140474557, -58.392307158181815],
        "Tribunales": [-34.60176154833913, -58.38456093858365],
        "9 de Julio": [-34.60453888530524, -58.38014065809253],
        "Catedral": [-34.60757221396939, -58.37419688300631],
    },
    "LINEA_E": {
        "Pichincha": [-34.62304099718662, -58.39710097116426],
        "Entre Ríos": [-34.62270550042393, -58.391489789929345],
        "San José": [-34.62224639739259, -58.385224149714155],
        "Independencia_E": [-34.61812318513492, -58.380224512115895],
        "Belgrano": [-34.6128518852584, -58.37787489702144],
        "Bolívar": [-34.60961123829135, -58.37401251606132],
    },
}



"""
Una vez tenemos las coordenadas vamos a aplicar la fórmula de Haversine que nos permite
calcular la distancia entre dos puntos geográficos
"""
#Ya importamo la función haversine
conexiones = []
# Recorrer cada línea y calcular distancias entre estaciones consecutivas
for linea, estaciones in LISTA_COORDENADAS.items():
    estaciones_nombres = list(estaciones.keys())
    for i in range(len(estaciones_nombres) - 1):
        estacion1 = estaciones_nombres[i]
        estacion2 = estaciones_nombres[i + 1]
        coord1 = estaciones[estacion1]  # Coordenadas de la primera estación
        coord2 = estaciones[estacion2]  # Coordenadas de la segunda estación
        # Calcular la distancia entre estaciones consecutivas
        distancia = haversine(coord1[0], coord1[1], coord2[0], coord2[1])
        # Añadir a la lista de conexiones
        conexiones.append((estacion1, estacion2, distancia))

# Mostrar las conexiones calculadas
for conexion in conexiones:
    print(f"{conexion[0]} -> {conexion[1]}: {conexion[2]:.2f}")

