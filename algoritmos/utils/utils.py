# Decorador para calcular el tiempo de ejecución de una función

from time import time

def calcular_tiempo(funcion):
    def wrapper(*args, **kwargs):
        inicio = time()
        resultado = funcion(*args, **kwargs)
        final = time()
        print(f"Tiempo de ejecución: {final - inicio}")
        return resultado
    return wrapper