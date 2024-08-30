# Importando modulo de Teste
import unittest

# Definir Variáveis
numero = -30

# Processamento de Dados
resultado = abs(numero)

# Saída de Dados
print(f"Valor Absoluto de {numero} é {resultado}")

def absoluto(a):
    return abs(a)

# Criando Classe que será usada para organizar e executar os testes
class TestAbsolutoFunction(unittest.TestCase):
    def test_absoluto_positive_numbers(self):
        self.assertEqual(absoluto(30), 30) # self.assertEqual(A, B) - Verifica se A é igual a B

    def test_absoluto_negative_numbers(self):
        self.assertEqual(absoluto(-27), 27)

# Executar os Testes
if __name__ == '__main__': # Executa apenas quando o script é executado diretamente
    unittest.main()