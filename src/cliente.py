class Cliente:
    def __init__(self, nome, sobrenome, cpf, nascimento, email, celular):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.nascimento = nascimento
        self.email = email
        self.celular = celular

    def cadastrar(self):
        cliente1 = Cliente('Lucas', 'Pereira', '246.436.460-63', '13/04/1987', 'lucaspereira@hotmail.com',
                           '(24) 99671-8837')
        return cliente1


    def exibir_cliente(self):
        print(f'Nome: {self.nome}')
        print(f'Sobrenome: {self.sobrenome}')
        print(f'CPF: {self.cpf}')
        print(f'Nascimento: {self.nascimento}')
        print(f'E-mail: {self.email}')
        print(f'Celular: {self.celular}')