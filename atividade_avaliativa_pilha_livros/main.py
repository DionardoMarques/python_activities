#Trabalho pilha com livros - Dionardo Marques / Algoritmos e Programação II
#Construindo a classe nó
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

#Construindo a classe pilha
class Pilha:
    def __init__(self):
        self.topo = None
        self._tamanho = 0

    #Criando um método para inserir o(s) livro(s)
    def adicionar(self, item):
        no = No(item)
        # proximo = quem está abaixo da pilha
        no.proximo = self.topo
        self.topo = no
        self._tamanho = self._tamanho + 1

    #Criando um método para remover o(s) livro(s) do topo da pilha
    def remover(self):
        if self._tamanho > 0:
            no = self.topo
            self.topo = self.topo.proximo
            self._tamanho = self._tamanho - 1
            return no
        raise IndexError("A pilha está vazia!")

    #Criando um método para retornar o valor do topo da pilha sem remover
    def verificar(self):
        if self._tamanho > 0:
            return self.topo.dado
        raise IndexError("A pilha está vazia!")

    def __len__(self):
        "Retorna o tamanho da lista"
        return self._tamanho

    def __repr__(self):
        d = ""
        cursor = self.topo
        while(cursor):
            d = d + str(cursor.dado) + "\n"
            cursor = cursor.proximo
        return d

    def __str__(self):
        return self.__repr__()

#Construindo a classe livro com seus três atributos (id, título e autor)
class Livro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor

    def imprimir(self):
        print("Título do livro: "+self.titulo)

    def getAutor(self):
        return self.autor

#Construindo a classe autor com seus dois atributos (id e nome)
class Autor:
    def __init__(self, id, nome):
        self._id = id #atributo fracamente privado
        self.nome = nome #atributo público

    def getNome(self):
        return self.nome

    def imprimir(self):
        print("Nome do autor: "+self.nome)

#Criando uma fila
pilha = Pilha()

#Criando o autor
autor1 = Autor(1, "Stephen Hawking")

#Criando os livros para popular
livro1 = Livro(1, "Uma Breve História no Tempo", autor1)
livro2 = Livro(2, "O Universo Numa Casca de Noz", autor1)
livro3 = Livro(3, "Buracos Negros", autor1)
livro4 = Livro(4, "Breves Respostas Para Grandes Questões", autor1)
livro5 = Livro(5, "Desvendando O Universo", autor1)

#Adicionando os livros a fila
pilha.adicionar(livro1)
pilha.adicionar(livro2)
pilha.adicionar(livro3)
pilha.adicionar(livro4)
pilha.adicionar(livro5)

#Removendo da fila
pilha.remover()
pilha.remover()

print(pilha)