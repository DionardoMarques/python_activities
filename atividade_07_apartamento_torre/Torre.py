#Classe Torre
class Torre():

    def __init__(self, id = 0, nome = None, endereco = None):

        self.id = id
        self.nome = nome
        self.endereco = endereco

    def cadastrar(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def imprimir(self):
        print("A torre de id", self.id, "com o nome", self.nome, "possui o seguinte endereço:", self.endereco)