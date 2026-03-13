# Módulo utilitário responsável por funções auxiliares da interface
# do sistema de estoque (limpar tela, mostrar menu e mensagens).


import os
from time import sleep


def limpartela():
    """
    Limpa o terminal do usuário.

    Funciona em diferentes sistemas operacionais:
    - Windows -> cls
    - Linux/Mac -> clear
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def saudacao():
    """
    Mostra a mensagem de boas-vindas do sistema.
    """
    print("=-"*12)
    print("   Bem vindo ao Sinc")
    print("=-"*12)
    # Pequena pausa para melhorar a experiência visual
    sleep(0.5)


def print_opcoes():
    """
    Mostra o menu principal com as opções do sistema.
    """
    print('''01 - Cadastrar Produto.
02 - Listar Produtos.
03 - Atualizar Produto.
04 - Remover Produtos.
05 - Sair do Programa.''')
    print("=-"*12)


def final_programa():
    
    """
    Mostra a mensagem de encerramento do programa.
    """
    print("=-"*21)
    print(" Sinc versão 1.0 criado por Breno Rossi ")
    print("=-"*21)
    # Aguarda alguns segundos antes de fechar o programa
    sleep(3)

