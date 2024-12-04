class Produto:
    def __init__(self, nome, preco, descricao, marca, modelo):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.marca = marca
        self.modelo = modelo
        self.produtos_cadastrados = []

    def cadastrar(self):
        nome = input('Digite o nome do produto automotivo: ')

        preco = float(input('Digite o preço do produto: '))

        descricao = input('Digite a descrição do produto: ')

        marca = input('Digite a marca do produto: ')

        modelo = input('Digite o modelo do produto: ')

        produto = Produto(nome, preco, descricao, marca, modelo)

        self.produtos_cadastrados.append(produto)