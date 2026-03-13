
# Módulo responsável por carregar e salvar os dados do estoque
# em um arquivo JSON que funciona como banco de dados simples.

import json
import os
# Nome do arquivo que armazenara os dados do estoque
ARQUIVO = 'ESTOQUE.json'

def carregar():
    """
    Carrega os dados do arquivo JSON.

    Se o arquivo não existir, cria uma estrutura padrão
    contendo o contador de IDs e um dicionário vazio de produtos.
    """

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


def salvar(dados):
    """
    Salva os dados do estoque no arquivo JSON.

    Parâmetros:
        dados (dict): estrutura do banco contendo produtos e proximo_id.
    """

    # abre o arquivo em modo escrita
    with open(ARQUIVO, 'w') as f:
        # converte o docionario python para json formatado.
        json.dump(dados, f, indent=4)