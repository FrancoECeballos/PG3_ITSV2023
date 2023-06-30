import unittest
from MediaYDesviaciónEJ4 import MediayDesviación

class Test_estandar(unittest.TestCase):
    def setUp(self) -> None:
        self.est = MediayDesviación()


    def test_estandar(self):
        resultado = self.est.calculate_statistics([4, 5, 8, 9, 10])
        self.assertEqual(resultado, (7.2, 2.3151673805580453))

if __name__ == "main":
    unittest.main()