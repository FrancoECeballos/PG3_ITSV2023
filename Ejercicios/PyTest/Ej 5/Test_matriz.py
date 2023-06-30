import unittest
from MatrizEJ5 import Matriz

class Test_matriz(unittest.TestCase):
    def setUp(self) -> None:
        self.mat = Matriz()


    def test_matriz(self):
        resultado = self.mat.search_matrix([4, 5, 8, 9, 10], 2)
        self.assertFalse(resultado)

if __name__ == "main":
    unittest.main()