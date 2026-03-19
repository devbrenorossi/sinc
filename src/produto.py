class Produtos:
    def __init__(self, nome, quantidade):
        self.nome = nome.upper()
        self.quantidade = quantidade

    def transforma_dic(self):
        return {
            "nome": self.nome,
            "quantidade": self.quantidade
        }
    
