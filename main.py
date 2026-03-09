import os
from time import sleep 

# Limpartela limpa o terminal cada vez que muda a opcao.
def limpartela():
    os.system('cls' if os.name == 'nt' else 'clear')

# variavel estoque armazena os produtos.
estoque = {}
# proximo_id variavel para sempre mostrar um ID nos produtos e nunca repetir.
proximo_id = 1

# while principal com o Menu.
while True:
    limpartela()
    # Apresentacao do programa com o nome.
    print("=-"*12)
    print("    Bem vindo ao Sinc")
    print("=-"*12)
    sleep(0.5)
    # print com as informacoes do programa.
    print('''01 - Cadastrar Produto.
02 - Listar Produtos.
03 - Atualizar Produto.
04 - Remover Produtos.
05 - Sair do Programa.''')
    print("=-"*12)

    try:
        # variavel escolha armazena a escolha do usuario.
        escolha = int(input('O que deseja fazer? '))
        limpartela()
        if escolha <= 0 or escolha >= 6:
            print("digite de 1 a 5")
            sleep(1.5)
            limpartela()
            continue

    except ValueError:
            limpartela()
        # tratamento de erro se o usuario digitar letras.
            print('Digite somente numeros...')
            sleep(3)
            limpartela()
            continue

    # cadastro de produto.
    if escolha == 1:
        try:
            nome_produto = input("Digite o nome do produto: ").title()
            produto_exite = False
            # verifica se o produto existe em estoque, se existir avisa que ja tem cadastrado.
            for dado in estoque.values():
                if dado["nome"] == nome_produto:
                    print('este produto ja esta cadastrado.')
                    print('Precione ENTER para sair...')
                    input()
                    limpartela()

                    produto_exite = True
                    break

            if produto_exite:
                continue

            # se nao existir o programa continua.
            quantidade_produto = int(input("Digite a quantidade do produto: "))
            estoque[proximo_id] = {
                    "nome": nome_produto, 
                    "quantidade": quantidade_produto
                }

            print(f"{nome_produto} - {quantidade_produto}, adicionado com sucesso....")
            proximo_id += 1
                    

            print('Precione ENTER para sair...')
            input()
            limpartela()
            continue

        except ValueError:
            print('Digite somente numeros...')
            print('Precione ENTER para sair...')
            input()
            limpartela()
            continue


    # listar produtos
    elif escolha == 2:

        # se nao tiver produto cadastrado ele informa.
        if not estoque:
            print('lista vazia, adicione produtos para conseguir vizualizar.')
            print('Precione ENTER para sair...')
            input()
            limpartela()

        # se tiver ele mostra na tela.
        else:
            for id, dados in estoque.items():
                print(f'{id} - "nome": {dados["nome"]} - "quantidade": {dados["quantidade"]}')
            print('Precione ENTER para sair...')
            input()
            limpartela()

    # Atualiza o produto.
    elif escolha == 3:
        try:
            id_produto = int(input('Digite o ID do produto: '))
            limpartela()
        
            # Se o ID nao existir
            if id_produto not in estoque:
                print('ID nao encontrado....')
                print('Precione ENTER para sair...')
                input()
                limpartela()
                continue

        except ValueError:
            print("digite somente numeros.")
            print('Precione ENTER para sair...')
            input()
            limpartela()

        # Atualiza o ID informado
        else:
            estoque[id_produto]["nome"] = input('Digite novo nome: ').title()
            try:
                estoque[id_produto]["quantidade"] = int(input('Digite a nova quantidade: '))

                print('produto atualizado com sucesso....')
                print('Precione ENTER para sair...')
                input()
                limpartela()
                
            except ValueError:
                print("digite somente numeros.")
                print('Precione ENTER para sair...')
                input()

    # remover um produto.
    elif escolha == 4:

        # se estoque vazio
        if not estoque:
            print('estoque vazio, adicione produtos..')
            print('Precione ENTER para sair...')
            input()
        
        # se tiver produto aqui ele remove.
        else:
            id_produto = int(input('digite o ID do produto a remover. '))
            
            if id_produto in estoque:
                nome_removido = estoque[id_produto]["nome"]

                del estoque[id_produto]

                print(f'{nome_removido}, Removido com sucesso....')
                print('Precione ENTER para sair...')
                input()
                limpartela()

            # se nao encontrar produto
            else:
                print('Produto nao encontrado....')
                print('Precione ENTER para sair...')
                input()
    
    # Aqui encerra o programa
    else:
        print("=-"*21)
        print(" Sinc version 1.0 criado por Breno Rossi ")
        print("=-"*21)
        sleep(3)
        break