import os
from time import sleep 

from modulos.functions import cadastrar_produto, listar_produto, atualizar_produto, remover_produto
from modulos.utils import limpartela, saudacao, print_opcoes, final_programa 
from database import carregar


# Carrega os dados do arquivo json
database = carregar()

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
        cadastrar_produto(database)


    elif escolha == 2:
        listar_produto(database)


    elif escolha == 3:
        atualizar_produto(database)


    elif escolha == 4:
        remover_produto(database)

# exibe uma mensagem de fechamento.
    else:
        final_programa()
        break