# Importando modulo de Teste
import unittest

# Definir Variáveis
texto1 = "A B C D"
texto2 = " E F G H"


# Processamento de Dados
resultado = texto1 + " com o" + texto2 + " é " + texto1 + texto2 

# Saída de Dados
print("a junção dos textos " + resultado)


def conc(a,b):
    return str(a) + str(b)

# Criando Classe que será usada para organizar e executar os testes
class TestConcatenacaoFunction(unittest.TestCase):
    # Método de Teste (Devem começar com test_)
    def test_conc_text(self):
        self.assertEqual(conc("AAA", " BBB"), "AAA BBB") # self.assertEqual(A, B) - Verifica se A é igual a B

# Executar os Testes
if __name__ == '__main__': # Executa apenas quando o script é executado diretamente
    unittest.main()