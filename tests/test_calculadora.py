import unittest

from src.calculadora import Calculadora


class TesteCalculadora(unittest.TestCase):

    def teste_adicao_falha(self):
        """
            Teste para o método adicionaComFalha da Classe Calculadora
            O teste falha, pois a implementação do método retorna None
        """
        calculadora = Calculadora()
        resultado = calculadora.adicionaComFalha(2, 3)
        self.assertEqual(resultado, 5)

        if __name__ == '__main__':
            unittest.main(argv=['first-arg-is-ignored'], exit=False)

    def teste_adicao(self):
        """
            Teste para o método adiciona da Classe Calculadora
            O teste deve passar, pois a implementação do método retorna a soma
        """
        calculadora = Calculadora()
        resultado = calculadora.adiciona(2, 3)
        self.assertEqual(resultado, 5)

    def teste_subtracao(self):
        """
            Teste para o método subtrai da Classe Calculadora
            O teste deve passar, pois a implementação do método retorna a soma
        """
        calculadora = Calculadora()
        resultado = calculadora.subtrai(5, 3)
        self.assertEqual(resultado, 2)

        if __name__ == '__main__':
            """
                Configuração do ambiente de teste e execução
                O teste criado na célula anterior falhará, indicando que a implementação atual não está correta
            """
            unittest.main(argv=['first-arg-is-ignored'], exit=False)
