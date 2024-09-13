import unittest

def soma(a,b):
    return a+b
        #⬇️ Classe
class TesteSomaFunction(unittest.TestCase):
    def test_soma_positivo(self):
        self.assertEqual(soma(3,2), 5)

    def test_soma_negativo(self):
        self.assertEqual(soma(-3,-2), -5)  # (-3) + (-2) = -5 

    def test_soma_misto(self):
        self.assertEqual(soma(3,-2), 1)

if __name__ == '__main__':
    unittest.main()