# Arquivo responsável pelas funções de CRUD do sistema de estoque.
# CRUD = Create, Read, Update, Delete (Cadastrar, Listar, Atualizar, Remover)

import modulos.utils as fun
from database import salvar


def cadastrar_produto(database):
    """
    Cadastra um novo produto no banco de dados. (Json)

    Parâmetros:
        database (dict): estrutura que contém os produtos e o próximo ID disponível.
    """
    try:
        # Solicita o nome do produto e padroniza para maiúsculo
        nome_produto = input("Digite o nome do produto: ").upper()
        # verifica se ja existe um produto com o mesmo nome
        for produto in database["produtos"].values():
            if produto["nome"] == nome_produto:
                print('este produto ja esta cadastrado.')
                print('Pressione ENTER para sair...')
                input()
                fun.limpartela()
                return
        # solicita a quantidade do produto
        quantidade_produto = int(input("Digite a quantidade de produto: "))

        # gera automaticamente o ID usando o contador do banco
        id_produto = str(database["proximo_id"])
        
        # adiciona o novo produto no dicionario de produtos
        database["produtos"][id_produto] = {
    "nome": nome_produto,
    "quantidade": quantidade_produto
}
        # atualiza o contador para o proximo produto
        database["proximo_id"] += 1

        # salva as alteracoes no arquivo (JSON)
        salvar(database)

    # tratamento de erro caso o usuario digite algo que nao seja numero.
    except ValueError:
        print('Digite somente numeros...')
        print('Precione ENTER para sair...')
        input()
        fun.limpartela()
        
    return


def listar_produto(database):
    """
    Lista todos os produtos cadastrados no estoque.
    """
    # Acessa o dicionario de produtos dentro do database
    produtos = database["produtos"]

    # verifica se existe algum produto cadastrado
    if not produtos:
        print('lista vazia, adicione produtos para conseguir vizualizar.')
        print('Precione ENTER para sair...')
        input()
        fun.limpartela()
        return

    # percorre todos os produtos e mostra na tela
    for id_produto, produto in produtos.items():
        print(f'ID: {id_produto} | Nome: {produto["nome"]} | Quantidade: {produto["quantidade"]}')
    print('Precione ENTER para sair...')
    input()
    fun.limpartela()


def atualizar_produto(database):
    """
    Atualiza as informacoes de um produto existente.
    """
    produtos = database["produtos"]

    # mostra todos os produtos antes de pedir o ID
    for id_produto, produto in produtos.items():
            print(f'ID: {id_produto} | Nome: {produto["nome"]} | Quantidade: {produto["quantidade"]}')

    # solicita o ID do produto que sera atualizado
    id_produto = input('Digite o ID do produto para atualizar: ')
    fun.limpartela()

    # verifica se existem produtos cadastrados
    if not produtos:
        print("Nenhum produto cadastrado....")
        print('Precione ENTER para sair...')
        input()
        fun.limpartela()
        return

    # verifica se o ID digitado existe
    if  id_produto not in produtos:
        print('ID nao encontrado....')
        print('Precione ENTER para sair...')
        input()
        fun.limpartela()
        return
        
    # solicita o novo nome do produto
    novo_produto = input('Digite novo nome: ').upper()
    
    # verifica se ja existe outro produto com esse nome
    for produto in produtos.values():
        if produto["nome"] == novo_produto:
            print('este produto ja esta cadastrado.')
            print('Pressione ENTER para sair...')
            input()
            fun.limpartela()
            return
        
    # atualiza o nome do produto
    produtos[id_produto]["nome"] = novo_produto
    
    try:
        # atualiza a quantidade de produto.
        produtos[id_produto]["quantidade"] = int(input('Digite a nova quantidade: '))
        print('produto atualizado com sucesso....')
        print('Precione ENTER para sair...')
        input()
        fun.limpartela()
        
    # tratamento caso o usuario digite texto na quantidade
    except ValueError:
        print("digite somente numeros.")
        print('Precione ENTER para sair...')
        input()
    # salva as alteracoes no arquivo
    salvar(database)


def remover_produto(database):
    """
    Remove um produto do estoque usando o ID
    """

    produtos = database["produtos"]

    # Mostra todos os produtos disponíveis
    for id, dados in produtos.items():
            print(f'ID = {id} | "nome": {dados["nome"]} | "quantidade": {dados["quantidade"]}')

    # verifica se o estoque esta vazio
    if not produtos:
        print('lista vazio, adicione produtos..')
        print('Precione ENTER para sair...')
        input()

    # solicita o ID do produto a ser removido
    id_produto = input('digite o ID do produto a remover. ')
    
    # verifica se o ID existe
    if id_produto in produtos:
        # guarda o nome antes de remover para mostrar msg
        nome_removido = produtos[id_produto]["nome"]

        # remove o produto do discionario
        del produtos[id_produto]

        print(f'{nome_removido}, Removido com sucesso....')
        print('Precione ENTER para sair...')
        input()
        fun.limpartela()

    # caso o id nao seja encontrado
    else:
        print('Produto nao encontrado....')
        print('Precione ENTER para sair...')
        input()
     
    # salva o banco apos a remocao
    salvar(database)

