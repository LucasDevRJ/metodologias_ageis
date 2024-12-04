# Criação da classe Produto
class Produto:
    # Construtor do Produto com seus atributos a serem instanciados
    def __init__(self, nome, preco, descricao, marca, modelo):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.marca = marca
        self.modelo = modelo

    # Método para cadastrar o Produto, passando seus valores nos construtores
    def cadastrar(self):
        produto1 = Produto('Kit Lavagem', 266.99, 'Kit Lavagem Automotiva Completa Profissional Produtos Vonixx',
                           'Vonixx', 'Lavagem Automotiva')
        produto2 = Produto('Detergente', 49.99, 'Detergente Automotivo Realeza 5 Litros', 'Realeza', '5 Litros')
        produto3 = Produto('Maquiador', 66.99, 'Maquiador Automotivo Renova Pintura E Defeitos Makker Vonixx', 'Vonixx',
                           'makker')

        produtos_cadastrados = [produto1, produto2, produto3]
        return produtos_cadastrados

    # Método para exibir os valores dos atributos da classe Produto
    def exibir_produto(self):
        print(f'Nome: {self.nome}')
        print(f'Preço: R$ {self.preco}')
        print(f'Descrição: {self.descricao}')
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
