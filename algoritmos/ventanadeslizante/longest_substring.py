
from typing import List

def solucion_fuerza_bruta(texto):
    """
    """
    # tomo el caracter y verifico si esta en una sublista
    # si esta en la sublista, entonces guardo el tamaño de la sublista
    tamaño_maximo = 0
    for i in range(len(texto)):
        sublista = ""
        for j in range(i, len(texto)):
            if texto[j] in sublista:
                if len(sublista) > tamaño_maximo:
                    tamaño_maximo = len(sublista)
                break
            sublista += texto[j]
    return tamaño_maximo

# Por ejemplo para la cadena "abcabcbb"
# este seria el paso a paso de la iteracion
# resultado = []
# sublista = ""
# i = 0
# j = 0
# texto[j] = a
# sublista = a
# j = 1
# texto[j] = b
# sublista = ab
# j = 2
# texto[j] = c
# sublista = abc
# j = 3
# texto[j] = a
# break
# resultado = [3]
# sublista = ""
# i = 1
# j = 1
# texto[j] = b
# sublista = b
# j = 2
# texto[j] = c
# sublista = bc
# j = 3
# texto[j] = a
# sublista = bca
# j = 4
# texto[j] = b
# break

def solucion_ventana_deslizante(texto):
    """
    Esta solucion no es completamente funcional, tiene el problema de que no funcionaria
    para caracterres repetidos
    """
    tamaño_maximo = 0
    sublista = ""
    for i in range(len(texto)):
        if texto[i] in sublista:
            if len(sublista) > tamaño_maximo:
                tamaño_maximo = len(sublista)
            sublista = sublista[sublista.index(texto[i]) + 1:]
            # aqui hay dos opciones, o bien se puede usar el metodo index
            # o se puede usar un indice "inicio" y "fin" para recorrer la
            # sublista
        sublista += texto[i]
    return tamaño_maximo

def solucion_ventana_deslizante(texto):
    """
    """
    inicio_ventana = 0
    tamaño_maximo = 0
    for fin_ventana in range(len(texto)):
        # print(texto[inicio_ventana:fin_ventana])
        if len(set(texto[inicio_ventana:fin_ventana])) == len(texto[inicio_ventana:fin_ventana]):
            tamaño_maximo = max(tamaño_maximo, fin_ventana - inicio_ventana)
        else:
            inicio_ventana += 1
    return tamaño_maximo

        

# Por ejemplo para la cadena "abcabcbb"
# este seria el paso a paso de la iteracion
# i = 0
# [a, b, c, a, b, c, b, b]
#  ↑
# sublista = a
# tamaño_maximo = 1
# 
# i = 1
# [a, b, c, a, b, c, b, b]
#     ↑
# sublista = ab
# tamaño_maximo = 2
#
# i = 2
# [a, b, c, a, b, c, b, b]
#        ↑
# sublista = abc
# tamaño_maximo = 3
#
# i = 3
# [a, b, c, a, b, c, b, b]
#           ↑
# sublista = a
# tamaño_maximo = 3
#
# i = 4
# [a, b, c, a, b, c, b, b]
#              ↑
# sublista = ab
# tamaño_maximo = 3
#
# i = 5
# [a, b, c, a, b, c, b, b]
#                 ↑
# sublista = abc
# tamaño_maximo = 3
#
# i = 6
# [a, b, c, a, b, c, b, b]
#                    ↑
# sublista = b
# tamaño_maximo = 3
#
# i = 7
# [a, b, c, a, b, c, b, b]
#                       ↑
# sublista = b
# tamaño_maximo = 3
#

