import modulos.utils as fun


def cadastrar_produto(ESTOQUE, proximo_id):
    try:
        nome_produto = input("Digite o nome do produto: ").title()

        for produto in ESTOQUE.values():
            if produto["nome"] == nome_produto:
                print('este produto ja esta cadastrado.')
                print('Pressione ENTER para sair...')
                input()
                fun.limpartela()
                return proximo_id
            
        quantidade_produto = int(input("Digite a quantidade de produto: "))
        ESTOQUE[proximo_id] = {
    "nome": nome_produto,
    "quantidade": quantidade_produto
}
        
        listar_produto(ESTOQUE)

    except ValueError:
        print('Digite somente numeros...')
        print('Precione ENTER para sair...')
        input()
        fun.limpartela()
        
    return proximo_id + 1


def listar_produto(ESTOQUE):
    if not ESTOQUE:
        print('lista vazia, adicione produtos para conseguir vizualizar.')
        print('Precione ENTER para sair...')
        input()
        fun.limpartela()

        # se tiver ele mostra na tela.
    else:
        for id, dados in ESTOQUE.items():
            print(f'ID = {id} | "nome": {dados["nome"]} | "quantidade": {dados["quantidade"]}')
        print('Precione ENTER para sair...')
        input()
        fun.limpartela()


def atualizar_produto(ESTOQUE):
    for id, dados in ESTOQUE.items():
            print(f'ID = {id} | "nome": {dados["nome"]} | "quantidade": {dados["quantidade"]}')
    try:
        id_produto = int(input('Digite o ID do produto para atualizar: '))
        # limpartela()
        
    except ValueError:
        print("digite somente numeros.")
        print('Precione ENTER para sair...')
        input()
        fun.limpartela()
        return

            # Se o ID nao existir
    if id_produto not in ESTOQUE:
        print('ID nao encontrado....')
        print('Precione ENTER para sair...')
        input()
        fun.limpartela()
        return
            


        # Atualiza o ID informado
    else:
        ESTOQUE[id_produto]["nome"] = input('Digite novo nome: ').title()
        try:
            ESTOQUE[id_produto]["quantidade"] = int(input('Digite a nova quantidade: '))
            print('produto atualizado com sucesso....')
            print('Precione ENTER para sair...')
            input()
            fun.limpartela()
            
            
        except ValueError:
            print("digite somente numeros.")
            print('Precione ENTER para sair...')
            input()


def remover_produto(ESTOQUE):
    for id, dados in ESTOQUE.items():
            print(f'ID = {id} | "nome": {dados["nome"]} | "quantidade": {dados["quantidade"]}')
        # se estoque vazio
    if not ESTOQUE:
        print('estoque vazio, adicione produtos..')
        print('Precione ENTER para sair...')
        input()
    
        # se tiver produto aqui ele remove.
    else:
        id_produto = int(input('digite o ID do produto a remover. '))
        
        if id_produto in ESTOQUE:
            nome_removido = ESTOQUE[id_produto]["nome"]

            del ESTOQUE[id_produto]                

            print(f'{nome_removido}, Removido com sucesso....')
            print('Precione ENTER para sair...')
            input()
            fun.limpartela()

        # se nao encontrar produto
        else:
            print('Produto nao encontrado....')
            print('Precione ENTER para sair...')
            input()

