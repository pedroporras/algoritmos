import unittest
from algoritmos import dosapuntadores

class TestDosApuntadores(unittest.TestCase):

    def test_fuerza_bruta(self):
        numeros = [1, 2, 7, 11, 19]
        objetivo = 9
        self.assertEqual(dosapuntadores.solucion_fuerza_bruta(numeros, objetivo), [1, 2])

    def test_apuntadores(self):
        numeros = [1, 2, 7, 11, 19]
        objetivo = 9
        self.assertEqual(dosapuntadores.solucion_apuntadores(numeros, objetivo), [1, 2])

# numeros_1 = [1, 2, 7, 11, 19]
# objetivo_1 = 9
# print("El tiempo usado con fuerza bruta es: ")
# print(solucion_fuerza_bruta(numeros_1, objetivo_1))
# print("El tiempo usado con apuntadores es: ")
# print(solucion_apuntadores(numeros_1, objetivo_1))

# sample_100 = np.random.randint(1000, size=100)
# objetivo_100 = random.randint(1000, 2000)
# print("El tiempo usado con fuerza bruta es: ")
# print(solucion_fuerza_bruta(sample_100, objetivo_100))
# print("El tiempo usado con apuntadores es: ")
# print(solucion_apuntadores(sample_100, objetivo_100))


# sample_1000 = np.random.randint(1000, size=1000)
# objetivo_1000 = random.randint(1000, 2000)
# print("El tiempo usado con fuerza bruta es: ")
# print(solucion_fuerza_bruta(sample_1000, objetivo_1000))
# print("El tiempo usado con apuntadores es: ")
# print(solucion_apuntadores(sample_1000, objetivo_1000))