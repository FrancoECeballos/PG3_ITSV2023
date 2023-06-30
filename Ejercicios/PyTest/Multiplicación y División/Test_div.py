import unittest
from Calculadora import Calculadora

class Test_div(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculadora()


    def test_div(self):
        resultado = self.calc.div(10,5)
        self.assertEqual(resultado, 2)


if __name__ == "main":
    unittest.main()