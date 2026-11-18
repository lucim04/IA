# Calculadora de rutas del metro de Buenos Aires · A*

Aplicación web que calcula la mejor ruta entre dos estaciones del metro (Subte) de Buenos Aires usando el algoritmo **A\*** sobre un grafo de la red, y la muestra sobre un mapa interactivo junto con la distancia, el tiempo estimado, la hora de llegada y los transbordos.

Proyecto en grupo de la asignatura **Inteligencia Artificial** del Grado en Ciencia de Datos e Inteligencia Artificial (Universidad Politécnica de Madrid).

## Qué hace

- El usuario elige **estación de origen, estación de destino, fecha y hora** de salida.
- La app comprueba que el metro esté **en servicio** a esa hora, con horarios distintos para laborables, sábados y domingos o festivos argentinos.
- Calcula la ruta con **A\*** y muestra:
  - el recorrido dibujado sobre el mapa de la ciudad,
  - la distancia total y el tiempo estimado de viaje,
  - la hora de llegada,
  - las estaciones en las que hay que hacer transbordo.

## Cómo funciona

**1. Modelado de la red como grafo** (`networkx`)
- Cada **estación** es un nodo con sus coordenadas reales (latitud y longitud) de las líneas A, B, C, D y E.
- Las estaciones consecutivas de una misma línea se unen con aristas cuyo peso es la **distancia real** entre ellas, calculada con la **fórmula de Haversine** (que tiene en cuenta la curvatura de la Tierra).
- Los **transbordos** entre líneas son aristas especiales con una pequeña penalización, para que el algoritmo no cambie de línea sin necesidad.

**2. Búsqueda con A\***
- La heurística es la **distancia en línea recta (Haversine)** entre la estación actual y el destino. Como nunca sobreestima la distancia real por la red, es admisible y A\* devuelve el camino óptimo.
- `MetroBAtiempo.py` es una variante que optimiza el **tiempo** en lugar de la distancia: el peso de cada arista es el tiempo de trayecto (según la velocidad media de cada línea) y la heurística divide la distancia en línea recta entre la velocidad máxima de la red, para que siga siendo admisible.

**3. Estimación del tiempo**
- Cada tramo se convierte a minutos con la **velocidad media de su línea**, y cada transbordo suma un tiempo fijo de cambio de andén.

**4. Interfaz** (`Streamlit` + `Folium`)
- Formulario de origen, destino, fecha y hora, con validación de entradas y de horario.
- Mapa interactivo con las estaciones coloreadas por línea y la ruta resaltada.

## Estructura

```
├── FIN/
│   ├── MetroBA.py           # App principal: ruta más corta en distancia
│   └── MetroBAtiempo.py     # Variante: ruta más rápida en tiempo
├── Datos/                   # Coordenadas, distancias, velocidades y transbordos de la red
├── Algoritmo/
│   └── Algoritmo.ipynb      # Desarrollo y pruebas del algoritmo
└── requirements.txt
```

## Cómo ejecutarlo

```bash
pip install -r requirements.txt
cd FIN
streamlit run MetroBA.py          # ruta más corta en distancia
streamlit run MetroBAtiempo.py    # ruta más rápida en tiempo
```

Se abrirá la app en el navegador (por defecto en `http://localhost:8501`).

## Tecnologías

Python · NetworkX · Streamlit · Folium · Matplotlib

## Equipo

Proyecto desarrollado de forma conjunta por:

- Laura García González
- Lucía Martínez Miramontes
- Ada Moral Merino
- Antía Sande Fernandez
- Candela Espinar Paisan
- David García Prieto
