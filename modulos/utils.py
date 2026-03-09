import os
from time import sleep


def limpartela():
    os.system('cls' if os.name == 'nt' else 'clear')


def saudacao():
    print("=-"*12)
    print("   Bem vindo ao Sinc")
    print("=-"*12)
    sleep(0.5)


def print_opcoes():
    print('''01 - Cadastrar Produto.
02 - Listar Produtos.
03 - Atualizar Produto.
04 - Remover Produtos.
05 - Sair do Programa.''')
    print("=-"*12)


def final_programa():
    print("=-"*21)
    print(" Sinc versão 1.0 criado por Breno Rossi ")
    print("=-"*21)
    sleep(3)

