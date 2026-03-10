import os
from time import sleep 

from modulos.functions import cadastrar_produto, listar_produto, atualizar_produto, remover_produto
from modulos.utils import limpartela, saudacao, print_opcoes, final_programa 


# variavel estoque armazena os produtos.
ESTOQUE = {}
# proximo_id variavel para sempre mostrar um ID nos produtos e nunca repetir.
proximo_id = 1

# while principal com o Menu.
while True:
    limpartela()
    # Apresentacao do programa com o nome.
    saudacao()
    # print com as informacoes do programa.
    print_opcoes()
    try:
        # variavel escolha armazena a escolha do usuario.
        escolha = int(input('O que deseja fazer? '))
        limpartela()
        if escolha not in range(1,6):
            print("digite de 1 a 5")
            sleep(2.5)
            limpartela()
            continue

    except ValueError:
            limpartela()
            # tratamento de erro se o usuario digitar letras.
            print('Digite somente numeros ou (5) para sair...')
            sleep(2.5)
            limpartela()
            continue

    # cadastro de produto.
    if escolha == 1:
        proximo_id = cadastrar_produto(ESTOQUE, proximo_id)
    
    # listar produtos
    elif escolha == 2:
        listar_produto(ESTOQUE)

    # Atualiza o produto.
    elif escolha == 3:
        atualizar_produto(ESTOQUE)
  
    # remover um produto.
    elif escolha == 4:
        remover_produto(ESTOQUE)
    
    # Aqui encerra o programa
    else:
        final_programa()
        break