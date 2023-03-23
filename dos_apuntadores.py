from utils import calcular_tiempo
import numpy as np
import random
# Casos de uso de los apuntadores
# Podemos identificar este patrón cuando el problema 
# involucra una lista ordenada, hay un conjunto de 
# elementos(pares, triples o incluso subarreglos) y hay un valor 
# objetivo que encontrar o duplicados que remover.

# Problema
#
# Dada una lista de enteros, regresa los índices de los dos números que sumen un valor específico.
# Puedes asumir que sólo habrá una solución y que no puedes utilizar el mismo elemento dos veces.



# Solución basada en fuerza bruta
@calcular_tiempo
def solucion_fuerza_bruta(numeros, objetivo):
    """
    Esta solución es de complejidad O(n^2)
    """
    for i in range(len(numeros)):
        for j in range(len(numeros)):
            if numeros[i] + numeros[j] == objetivo:
                return [i, j]
            



# Solución
#
# Para resolver este problema, podemos utilizar dos apuntadores, uno al principio y otro al final.
# Si la suma de los dos elementos apuntados es menor que el objetivo, 
# entonces debemos incrementar el apuntador del principio.
# Si la suma de los dos elementos apuntados es mayor que el objetivo, 
# entonces debemos decrementar el apuntador del final.
# Si la suma de los dos elementos apuntados es igual al objetivo,
# entonces hemos encontrado la solución.
# Te explico, como la lista esta ordenada entonces cuando es menor el valor del apuntador del principio
# entonces debemos incrementarlo para que la suma sea mayor, y si es mayor el valor del apuntador del final
@calcular_tiempo
def solucion_apuntadores(numeros, objetivo):
    """
    Esta solución es de complejidad O(n)
    """
    inicio = 0
    final = len(numeros) - 1
    while inicio < final:
        suma = numeros[inicio] + numeros[final]
        if suma == objetivo:
            return [inicio, final]
        elif suma < objetivo:
            inicio += 1
        else:
            final -= 1

numeros_1 = [1, 2, 7, 11, 19]
objetivo_1 = 9
print("El tiempo usado con fuerza bruta es: ")
print(solucion_fuerza_bruta(numeros_1, objetivo_1))
print("El tiempo usado con apuntadores es: ")
print(solucion_apuntadores(numeros_1, objetivo_1))

sample_100 = np.random.randint(1000, size=100)
objetivo_100 = random.randint(1000, 2000)
print("El tiempo usado con fuerza bruta es: ")
print(solucion_fuerza_bruta(sample_100, objetivo_100))
print("El tiempo usado con apuntadores es: ")
print(solucion_apuntadores(sample_100, objetivo_100))


sample_1000 = np.random.randint(1000, size=1000)
objetivo_1000 = random.randint(1000, 2000)
print("El tiempo usado con fuerza bruta es: ")
print(solucion_fuerza_bruta(sample_1000, objetivo_1000))
print("El tiempo usado con apuntadores es: ")
print(solucion_apuntadores(sample_1000, objetivo_1000))