# Importando modulo de Teste
import unittest

# Definir Variáveis
numero1 = 2
numero2 = 3

# Processamento de Dados
resultado = numero1 + numero2

# Saída de Dados
print(f"A Soma de {numero1} e {numero2} é {resultado}")

def add(a,b):
    return a + b

# Criando Classe que será usada para organizar e executar os testes
class TestAddFunction(unittest.TestCase):
    # Método de Teste (Devem começar com test_)
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5) # self.assertEqual(A, B) - Verifica se A é igual a B

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-2, 3), 1)

# Executar os Testes
if __name__ == '__main__': # Executa apenas quando o script é executado diretamente
    unittest.main()