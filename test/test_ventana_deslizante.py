import unittest
from algoritmos import ventanadeslizante

class TestVentanaDeslizante(unittest.TestCase):

    def test_fuerza_bruta(self):
        """
        """
        calificaciones = [10.0, 7.8, 6.5, 8.0, 9.2]
        window_size = 3
        resultado = ventanadeslizante.solucion_fuerza_bruta(window_size, calificaciones)
        OBJETIVO = [8.1, 7.43, 7.9]
        self.assertEqual(resultado, OBJETIVO)

    def test_ventana_deslizante(self):
        """
        """
        calificaciones = [10.0, 7.8, 6.5, 8.0, 9.2]
        window_size = 3
        resultado = ventanadeslizante.solucion_ventana_deslizante(window_size, calificaciones)
        OBJETIVO = [8.1, 7.43, 7.9]
        self.assertEqual(resultado, OBJETIVO)