import unittest

def media(notas):
    return sum(notas) / len(notas)

class TestMultiFunction(unittest.TestCase):
    def test_media(self):
        self.assertEqual(media([1,2,3,4,5]), 3)

if __name__ == '__main__':
    unittest.main()