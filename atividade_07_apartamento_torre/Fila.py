#Classe Fila
from No import No

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def adicionar(self, valor):
        no = No(valor)

        if self.tamanho == 0:
            self.inicio = no
            self.fim = no
        else:
            self.fim.proximo = no
            self.fim = no
        self.tamanho += 1

    def remover(self):
        if self.tamanho == 0:
            print('Fila vazia.')
        elif self.tamanho == 1:
            self.inicio = None
            self.fim = None
            self.tamanho -= 1
        else:
            self.inicio = self.inicio.proximo
            self.tamanho -= 1

    def imprimir(self):
        texto = ""
        if self.tamanho == 0:
            print('Fila vazia.')
        else:
            aux = self.inicio
            while(aux):
                texto = texto + "ID:" + str(aux.dado.id) + " - Apto: " + str(aux.dado.num_apart) + " Torre: " + str(
                    aux.dado.torre.nome) + '\n'
                aux = aux.proximo

            print(texto)
            print("---------------------------")