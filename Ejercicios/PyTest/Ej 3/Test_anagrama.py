import unittest
from AnagramaEJ3 import Anagrama

class Test_anagrama(unittest.TestCase):
    def setUp(self) -> None:
        self.an = Anagrama()


    def test_anagrama(self):
        resultado = self.an.is_anagram("hola","aloh")
        self.assertTrue(resultado)

if __name__ == "main":
    unittest.main()