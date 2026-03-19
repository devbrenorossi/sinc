
from time import sleep 

from src.estoque import Estoque
from src.utils import limpartela, saudacao, print_opcoes, final_programa, mostrar_produto


# Carrega os dados do arquivo json
estoque = Estoque()

# loop principal que controla o menu do sistema.
while True:
    limpartela()
    saudacao()
    # mostra as opcoes do programa.
    print_opcoes()
    
    try:
        escolha = int(input('O que deseja fazer? '))
        limpartela()
        # ele fltra se o usuario digitou entre 1 e 5.
        if escolha not in range(1,6):
            print("digite de 1 a 5")
            sleep(2.5)
            limpartela()
            continue

    # tratamento de erro se o usuario digitar letras.
    except ValueError:
            limpartela()
            print('Digite somente numeros ou (5) para sair...')
            sleep(2.5)
            limpartela()
            continue


    if escolha == 1:
        nome = input("Digite o produto: ").upper()
        try:
            quantidade = float(input("Digite a quantidade: "))
        except ValueError:
            print("Digite somente numeros para a quantidade.")
            sleep(2)
            continue
        estoque.cadastrar_produto(nome, quantidade)


    elif escolha == 2:
        estoque.listar_produto()
        

    elif escolha == 3:
        mostrar_produto()

        # solicita o ID do produto que sera atualizado
        id_produto = input('Digite o ID do produto para atualizar: ')
       

        estoque.atualizar_produto(id_produto)


    elif escolha == 4:
        mostrar_produto()

        # solicita o ID do produto a ser removido
        id_produto = input('digite o ID do produto a remover. ')

        estoque.remover_produto(id_produto)


    # exibe uma mensagem de fechamento.
    else:
        final_programa()
        break