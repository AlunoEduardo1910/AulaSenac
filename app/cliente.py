
class Cliente:
    def __init__(self, nome, idade, ativo):
        self.nome = nome
        self.idade = idade
        self.ativo = ativo

    def pode_comprar(self):
        return self.ativo and self.idade >= 18

    def desativar(self):
        self.ativo = False

    def atualizar_idade(self, nova_idade):
        if nova_idade < 0:
            raise ValueError("Idade inválida")
        self.idade = nova_idade