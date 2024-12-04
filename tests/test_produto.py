from src import produto
from src.produto import Produto


def testar_metodo_cadastrar():
    produto = Produto('', 0.0, '', '', '')  # Criando uma instância da classe Produto (não importa os dados iniciais)
    produtos_cadastrados = produto.cadastrar()  # Chamando o método cadastrar

    # Verificando se os produtos foram cadastrados corretamente
    assert len(produtos_cadastrados) == 3  # Deve haver 3 produtos cadastrados
    assert produtos_cadastrados[0].nome == 'Kit Lavagem'  # Verificando o nome do primeiro produto
    assert produtos_cadastrados[1].preco == 49.99  # Verificando o preço do segundo produto
    assert produtos_cadastrados[2].marca == 'Vonixx'  # Verificando a marca do terceiro produto

    print("Testes realizados com sucesso!")
    produtos_cadastrados[0].exibir_produto()
    print('\n')
    produtos_cadastrados[1].exibir_produto()
    print('\n')
    produtos_cadastrados[2].exibir_produto()


# Executando o teste
testar_metodo_cadastrar()
