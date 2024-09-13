import unittest

def divisao(a,b):
    return a/b

class TesteDivisaoFunction(unittest.TestCase):
    def test_divisao_positivo(self):
        self.assertEqual(divisao(6,2), 3)

    def test_divisao_negativo(self):
        self.assertEqual(divisao(-12,-3), 4) # (-12) / (-3) = +4

    def test_divisao_misto(self):
        self.assertEqual(divisao(14,-7), -2)

if __name__ == '__main__':
    unittest.main()