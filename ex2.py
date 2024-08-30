# Importando modulo de Teste
import unittest

# Definir Variáveis
numero1 = 2
numero2 = 3

# Processamento de Dados
resultado = numero1 - numero2

# Saída de Dados
print(f"A Subtração de {numero1} - {numero2} é {resultado}")

def sub(a,b):
    return a - b

# Criando Classe que será usada para organizar e executar os testes
class TestSubFunction(unittest.TestCase):
    # Método de Teste (Devem começar com test_)
    def test_sub_positive_numbers(self):
        self.assertEqual(sub(2, 3), -1) # self.assertEqual(A, B) - Verifica se A é igual a B

    def test_sub_negative_numbers(self):
        self.assertEqual(sub(-2, -3), 1)

    def test_sub_mixed_numbers(self):
        self.assertEqual(sub(-2, 3), -5)

# Executar os Testes
if __name__ == '__main__': # Executa apenas quando o script é executado diretamente
    unittest.main()