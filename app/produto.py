class Produtos:


    def __init__(self,nome,preco,estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def adicionar_estoque(self,novo_estoque):
        self.estoque += novo_estoque
    def vender(self,quantidade_vendida):
        self.estoque -= quantidade_vendida
    def alterar_preco(self,novo_preco):
        self.preco = novo_preco
