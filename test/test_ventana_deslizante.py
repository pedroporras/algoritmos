import unittest
from algoritmos.ventanadeslizante import ventana_deslizante, longest_substring

class TestVentanaDeslizante(unittest.TestCase):

    def test_fuerza_bruta(self):
        """
        """
        print("test_fuerza_bruta")
        calificaciones = [10.0, 7.8, 6.5, 8.0, 9.2]
        window_size = 3
        resultado = ventana_deslizante.solucion_fuerza_bruta(window_size, calificaciones)
        OBJETIVO = [8.1, 7.43, 7.9]
        self.assertEqual(resultado, OBJETIVO)

    def test_ventana_deslizante(self):
        """
        """
        print("test_ventana_deslizante")
        calificaciones = [10.0, 7.8, 6.5, 8.0, 9.2]
        window_size = 3
        resultado = ventana_deslizante.solucion_ventana_deslizante(window_size, calificaciones)
        OBJETIVO = [8.1, 7.43, 7.9]
        self.assertEqual(resultado, OBJETIVO)

    def test_solucion_fuerza_bruta_longest_substring(self):
        """
        """
        print("test_solucion_fuerza_bruta_longest_substring")
        texto = "abcabcbb"
        resultado = longest_substring.solucion_fuerza_bruta(texto)
        OBJETIVO = 3
        self.assertEqual(resultado, OBJETIVO)

    def test_solucion_fuerza_bruta_longest_substring_2(self):
        """
        """
        texto = "jdkafnlcdsalkxcmpoiuytfccv"
        resultado = longest_substring.solucion_fuerza_bruta(texto)
        OBJETIVO = 15
        self.assertEqual(resultado, OBJETIVO)

    def test_longest_substring(self):
        """
        """
        print("test_longest_substring")
        texto = "abcabcbb"
        resultado = longest_substring.solucion_ventana_deslizante(texto)
        OBJETIVO = 3
        self.assertEqual(resultado, OBJETIVO)

    def test_longest_substring_2(self):
        """
        """
        print("test_longest_substring_2")
        texto = "jdkafnlcdsalkxcmpoiuytfccv"
        resultado = longest_substring.solucion_ventana_deslizante(texto)
        OBJETIVO = 15
        self.assertEqual(resultado, OBJETIVO)