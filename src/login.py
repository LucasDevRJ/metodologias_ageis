class Login:
    def autenticacao_falha(self, usuario, senha):
        # Etapa Red
        """
            Método para autenticar usuário
            Implementação inicial retorna False (Falha proposital)
        """
        return False

    def autenticacao_sucesso(self, usuario, senha):
        # Etapa Green
        """
            Método para autenticar usuário
            Implementação inicial retorna True
        """
        return True

    def autenticacao_vazia(self, usuario, senha):
        # Etapa Green
        """
            Método para autenticar usuário
            Implementação retorna True se o usuário e senha não forem vazios
        """
        return bool(usuario and senha)

    def autenticacao(self, usuario, senha):
        """
            Método para autenticar usuário
            Implementação inicial retorna False
        """
        return False

    def autenticacao_caracteres_especiais(self, usuario, senha):
        """
            Método para autenticar usuário
            Implementação retorna True se a senha contiver letras e números
        """
        return any(c.isalpha() for c in senha) and any(c.isdigit() for c in senha)
