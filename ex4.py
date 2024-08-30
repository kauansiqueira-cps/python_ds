# Importando modulo de Teste
import unittest

# Definir Variáveis
numero1 = 50
numero2 = 75


# Processamento de Dados
resultado = max(numero1,numero2)

# Saída de Dados
print(f"O maior numero entre {numero1} e {numero2} é {resultado}")

def maior(a,b):
    return max(a,b)

# Criando Classe que será usada para organizar e executar os testes
class TestMaiorFunction(unittest.TestCase):
    # Método de Teste (Devem começar com test_)
    def test_maior_positive_numbers(self):
        self.assertEqual(maior(30, 5), 30) # self.assertEqual(A, B) - Verifica se A é igual a B

    def test_maior_negative_numbers(self):
        self.assertEqual(maior(-27, -3), -3)

    def test_maior_mixed_numbers(self):
        self.assertEqual(maior(-2, 3), 3)

# Executar os Testes
if __name__ == '__main__': # Executa apenas quando o script é executado diretamente
    unittest.main()