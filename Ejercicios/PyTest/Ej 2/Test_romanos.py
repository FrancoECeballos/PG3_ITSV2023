import unittest
from RomanosEJ2 import Roman

class Test_romanos(unittest.TestCase):
    def setUp(self) -> None:
        self.roma = Roman()


    def test_romanos(self):
        resultado = self.roma.roman_to_decimal("MMMCMLXXXVI")
        self.assertEqual(resultado, 3986)

if __name__ == "main":
    unittest.main()