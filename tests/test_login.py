import unittest

from src.login import Login

class TesteLogin(unittest.TestCase):
    def teste_autenticacao_sucesso(self):
        """
            Teste para autenticação bem-sucedida
            O teste falha, pois a implementação do método autenticacao retorna false
        """
        login = Login()
        resultado = login.autenticacao_sucesso("usuario", "senha")
        self.assertTrue(resultado)

    def teste_autenticacao_falha(self):
        """
            Teste para autenticação mal-sucedida
            O teste falha, pois a implementação do método autenticacao retorna false
        """
        login = Login()
        resultado = login.autenticacao_falha("usuario", "senha_incorreta")
        self.assertFalse(resultado)

    def teste_autenticacao_vazia(self):
        """
            Teste para autenticação de credenciais vazias
            O teste falha, pois a implementação do método autenticacao ainda não valida credenciais vazias
        """
        login = Login()
        resultado = login.autenticacao_vazia("", "")
        self.assertFalse(resultado)

    def teste_alfanumerico_login(self):
        """
            Teste para autenticação com senha letras e números
            O teste falha, pois a implementação atual não é válida nessa condiçõa
        """
        login = Login()
        resultado = login.autenticacao("usuario", "senha123")
        self.assertFalse(resultado)

    def teste_caracteres_especiais_senha(self):
        """
            Teste para autenticação com senha contendo caracteres especiais
            O teste irá falhar, porque a implementação atual não é válida para a condição
        """
        login = Login()
        resultado = login.autenticacao_caracteres_especiais("usuario", "senha@123")
        self.assertTrue(resultado)