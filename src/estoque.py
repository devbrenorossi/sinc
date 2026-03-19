import json
import os
from src.produto import Produtos
from time import sleep


ARQUIVO = "data/estoque.json"


class Estoque:
    def __init__(self):
        self.dados = self.carregar()


    def carregar(self):
        """
        Carrega os dados do arquivo JSON.

        Se o arquivo não existir, cria uma estrutura padrão
        contendo o contador de IDs e um dicionário vazio de produtos.
        """
        # cria a pasta se não existir
        os.makedirs("data", exist_ok=True)
        # Verifica se o arquivo do banco existe
        if not os.path.exists(ARQUIVO):
            # retorna estrutura inicial do banco
            return {
                "proximo_id": 1,
                "produtos": {}
            }
        # abre o arquivo JSON em modo leitura
        with open(ARQUIVO, 'r') as f:
            # converte o json para dicionario python
            return json.load(f)


    def salvar(self):
        """
        Salva os dados do estoque no arquivo JSON.

        Parâmetros:
            dados (dict): estrutura do banco contendo produtos e proximo_id.
        """

        # abre o arquivo em modo escrita
        with open(ARQUIVO, 'w') as f:
            # converte o docionario python para json formatado.
            json.dump(self.dados, f, indent=4)


    def cadastrar_produto(self, nome, quantidade):
        """
        Cadastra um novo produto no banco de dados. (Json)

        Parâmetros:
            produto (dict): estrutura que contém os produtos e o próximo ID disponível.
        """
            # verifica se ja existe um produto com o mesmo nome
        for produto in self.dados["produtos"].values():
            if produto["nome"] == nome.upper():
                print('este produto ja esta cadastrado.')
                print('Pressione ENTER para sair...')
                input()
                return

        # adiciona o novo produto no dicionario de produtos
        produto = Produtos(nome, quantidade)

        # gera automaticamente o ID usando o contador do banco
        id_produto = str(self.dados["proximo_id"])

        self.dados["produtos"][id_produto] = produto.transforma_dic()
        
        # atualiza o contador para o proximo produto
        self.dados["proximo_id"] += 1

        # salva as alteracoes no arquivo (JSON)
        self.salvar()


    def listar_produto(self):
        """
        Lista todos os produtos cadastrados no estoque.
        """
        # Acessa o dicionario de produtos dentro do database
        produtos = self.dados["produtos"]

        # verifica se existe algum produto cadastrado
        if not produtos:
            print('lista vazia, adicione produtos para conseguir vizualizar.')
            print('Precione ENTER para sair...')
            input()

        # percorre todos os produtos e mostra na tela
        for id_produto, produto in produtos.items():
            print(f'ID: {id_produto} | Nome: {produto["nome"]} | Quantidade: {produto["quantidade"]}')
        print('Precione ENTER para sair...')
        input()


    def atualizar_produto(self, id_produto):
        """
        Atualiza as informacoes de um produto existente.
        """
        produtos = self.dados["produtos"]
       
        # verifica se existem produtos cadastrados
        if not produtos:
            print("Nenhum produto cadastrado....")
            print('Precione ENTER para sair...')
            input()
            return


        # verifica se o ID digitado existe
        if  id_produto not in produtos:
            print('ID nao encontrado....')
            print('Precione ENTER para sair...')
            input()
            return

        novo_nome = input('Digite o novo nome: ').upper()

        try:
            nova_quantidade = float(input('Digite a nova quantidade: '))
        except ValueError:
            print("digite somente numeros.")
            sleep(2)

        # verifica se ja existe outro produto com esse nome
        for id, produto in produtos.items():
            if produto["nome"] == novo_nome and id != id_produto:
                print('este produto ja esta cadastrado.')
                print('Pressione ENTER para sair...')
                input()
                return

        # atualiza o nome do produto
        produtos[id_produto]["nome"] = novo_nome

        # atualiza a quantidade de produto.
        produtos[id_produto]["quantidade"] = nova_quantidade


        # salva as alteracoes no arquivo
        self.salvar()

        print('produto atualizado com sucesso....')


    def remover_produto(self, id_produto):
        """
        Remove um produto do estoque usando o ID
        """

        produtos = self.dados["produtos"]
        
        # verifica se o estoque esta vazio
        if not produtos:
            print('lista vazio, adicione produtos..')
            print('Precione ENTER para sair...')
            input()


        # verifica se o ID existe
        if id_produto in produtos:
            # guarda o nome antes de remover para mostrar msg
            nome_removido = produtos[id_produto]["nome"]

            # remove o produto do discionario
            del produtos[id_produto]

            print(f'{nome_removido}, Removido com sucesso....')
            print('Precione ENTER para sair...')
            input()

        # caso o id nao seja encontrado
        else:
            print('Produto nao encontrado....')
            print('Precione ENTER para sair...')
            input()
        
        # salva o banco apos a remocao
        self.salvar()



