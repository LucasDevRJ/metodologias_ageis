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
        self.assertIsNone(resultado, 5)

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

    def teste_subtracao(self):
        """
            Teste para o método subtrai da Classe Calculadora
            O teste deve passar, pois a implementação do método retorna a soma
        """
        calculadora = Calculadora()
        resultado = calculadora.subtraiComFalha(5, 3)
        self.assertIsNone(resultado, 2)