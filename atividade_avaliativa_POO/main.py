from abc import ABCMeta, abstractmethod
######################################################### Objeto Computador #######################################################
class Computador(metaclass=ABCMeta):
    @property
    def modelo(self, modelo):
        self.modelo = modelo

    @property
    def cor(self, cor):
        self.cor = cor

    @property
    def preco(self, preco):
        self.preco = preco

    def getinformacoes(self):
        Computador.modelo(self)
        Computador.cor(self)
        Computador.preco(self)

    @abstractmethod
    def cadastrar(self):
        pass

######################################################### Objeto Desktop #######################################################
class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        Computador.__init__(self, modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte

    def getinformacoes(self):
        Computador.modelo(self)
        Computador.cor(self)
        Computador.preco(self)
        Desktop._potenciaDaFonte(self)

######################################################### Objeto Notebook #######################################################
class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        Computador.__init__(self, modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    def getinformacoes(self):
        Computador.modelo(self)
        Computador.cor(self)
        Computador.preco(self)
        Notebook.__tempoDeBateria(self)