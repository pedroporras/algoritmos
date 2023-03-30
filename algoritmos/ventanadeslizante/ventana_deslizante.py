
from typing import List

# Por ejemplo, para una ventana de tamaño 3 y la siguiente lista [1, 2, 3, 4, 5]
# este seria el paso a paso de la iteracion
# resultado = []
# [1, 2, 3, 4, 5]
#  ↑
# sublista -> [1, 2, 3]
# resultado -> [2.0]
#
# [1, 2, 3, 4, 5]
#     ↑
# sublista -> [2, 3, 4]
# resultado -> [2.0, 3.0]
#
# [1, 2, 3, 4, 5]
#        ↑
# sublista -> [3, 4, 5]
# resultado -> [2.0, 3.0, 4.0]
#
def solucion_fuerza_bruta(window_size: int, calificaciones: List) -> List:
    """
    """
    result = []
    # La iteracion de la ventana se detiene cuando el indice de la ventana
    # mas el tamaño de la ventana sea mayor o igual al tamaño de la lista
    # de calificaciones
    # en otras palabras se calcula el tamaño de la lista de calificaciones
    # menos el tamaño de la ventana y se le suma 1 porque el indice de la
    # lista comienza en 0, otra opcion es usar el tamaño de la lista de
    # calificaciones menos el tamaño de la ventana y se le resta 1

    for i in range(len(calificaciones) - window_size + 1):
        subtotal = 0
        for item in calificaciones[i:i+window_size]:
            subtotal += item
        result.append(round(subtotal / window_size, 2))
    return result

# Por ejemplo, para una ventana de tamaño 3 y la siguiente lista [1, 2, 3, 4, 5]
# este seria el paso a paso de la iteracion
# suma_ventana = 0
# [1, 2, 3, 4, 5]
#  ↑
# suma -> 1
# suma_ventana -> 1
# inicio_ventana -> 0
# fin_ventana -> 0
# resultado -> []
#
# suma_ventana = 1
# [1, 2, 3, 4, 5]
#     ↑
# suma -> 2
# suma_ventana -> 3
# inicio_ventana -> 0
# fin_ventana -> 1
# resultado -> []
#
# suma_ventana = 3
# [1, 2, 3, 4, 5]
#        ↑
# suma -> 3
# suma_ventana -> 6
# inicio_ventana -> 1
# fin_ventana -> 2
# resultado -> [2.0]
# resta -> 1
# suma_ventana -> 5
#
# suma_ventana = 5
# [1, 2, 3, 4, 5]
#           ↑
# suma -> 4
# suma_ventana -> 9
# inicio_ventana -> 2
# fin_ventana -> 3
# resultado -> [2.0, 3.0]
# resta -> 2
# suma_ventana -> 7
#
# suma_ventana = 7
# [1, 2, 3, 4, 5]
#              ↑
# suma -> 5
# suma_ventana -> 12
# inicio_ventana -> 3
# fin_ventana -> 4
# resultado -> [2.0, 3.0, 4.0]
# resta -> 3
# suma_ventana -> 9
def solucion_ventana_deslizante(window_size: int, calificaciones: List):
    """
    """
    resultado = []
    # Inicializamos el contador que va a ir almacenando el total de la
    # ventana actual (seria la sublista que se esta iterando)
    suma_ventana = 0.0
    # Inicializamos el indice de inicio de la ventana
    inicio_ventana = 0
    
    # Iteramos sobre la lista de calificaciones
    for fin_ventana in range(len(calificaciones)):
        # Almacenamos el valor de la calificacion en la variable suma_ventana
        suma_ventana += calificaciones[fin_ventana]
        # Verificamos si el indice de la ventana actual es igual al tamaño de la ventana
        if fin_ventana >= (window_size - 1):
            # Calculamos el promedio de la ventana actual
            resultado.append(round(suma_ventana / window_size, 2))
            # Restamos el valor de la primera calificacion de la ventana actual
            # al valor de la variable suma_ventana
            suma_ventana -= calificaciones[inicio_ventana]
            # Incrementamos el indice de inicio de la ventana
            inicio_ventana += 1
    return resultado
