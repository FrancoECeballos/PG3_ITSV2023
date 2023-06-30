import unittest
from ValidaciónEJ1 import Validate

class Test_contraseña(unittest.TestCase):
    def setUp(self) -> None:
        self.val = Validate()


    def test_contraseña(self):
        resultado = self.val.validate_password("Elpepe123:")
        self.assertFalse(resultado)

if __name__ == "main":
    unittest.main()