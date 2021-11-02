#Classe Apartamento
from Torre import Torre

class Apartamento(Torre):
    def __init__(self, id=None, num_apart=None, num_garagem=None, torre=None):
        Torre.__init__(self, id, nome='', endereco='')

        self.num_apart = num_apart
        self.num_garagem = num_garagem
        self.torre = torre

    def cadastrar(self, id, num_apart, num_garagem, torre):
        self.id = id
        self.num_apart = num_apart
        self.num_garagem = num_garagem
        self.torre = torre

    def imprimir(self):
        print("O apartamento de id", self.id, "com número", self.num_apart, "possui a vaga de garagem",
              self.num_garagem, "e a sua torre é", self.torre.id)