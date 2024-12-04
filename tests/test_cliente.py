# Importando a Classe Cliente
from src.cliente import Cliente


# Método para testar o Cadastro do Cliente
def testar_metodo_cadastrar():
    # Instanciando o Cliente
    cliente = Cliente('', '', '', '', '', '')
    # Armazenando referência do Cliente
    cliente_cadastrado = cliente.cadastrar()

    # Validando tamanho do nome e sobrenome do cliente, para ver se é maior que zero
    assert len(cliente_cadastrado.nome) > 0
    assert len(cliente_cadastrado.sobrenome) > 0
    # Verificando se os dados do cliente possui caracteres essenciais nos valores
    assert '.' and '-' in cliente_cadastrado.cpf
    assert '/' in cliente_cadastrado.nascimento
    assert '@' and '.com' in cliente_cadastrado.email
    assert '-' and '(' and ')' in cliente_cadastrado.celular

    print("Testes realizados com sucesso!")
    # Exibindo dados do Cliente
    cliente_cadastrado.exibir_cliente()

# Chamando o método de cadastrar
testar_metodo_cadastrar()
