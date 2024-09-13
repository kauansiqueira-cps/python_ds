import unittest

def multi(a,b):
    return a * b

        # ⬇️⬇️⬇️ Classe
class TestMultiFunction(unittest.TestCase):
    def test_multi_positivo(self):
        self.assertEqual(multi(6,2), 12)

    def test_multi_negativo(self):
        self.assertEqual(multi(-3,-5), 15)

    def test_multi_misto(self):
        self.assertEqual(multi(9,-9), -81)

if __name__ == '__main__':
    unittest.main()