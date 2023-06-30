import unittest
from Calculadora import Calculadora

class Test_mult(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculadora()


    def test_mult(self):
        resultado = self.calc.mult(3,5)
        self.assertEqual(resultado, 15)


if __name__ == "main":
    unittest.main()