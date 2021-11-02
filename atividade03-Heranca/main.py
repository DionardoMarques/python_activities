class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def imprimir(self):
        print("Código:", self.codigo)
        print("Nome:", self.nome)
        print("Matrícula:", self.matricula)

class AlunoEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano

    def imprimir(self):
        Aluno.imprimir(self)
        print("Ano:", self.ano)

class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        Aluno.__init__(self, codigo, nome, matricula)
        self.semestre = semestre

    def imprimir(self):
        Aluno.imprimir(self)
        print("Semestre:", self.semestre)

#Running
x = AlunoEnsinoMedio("9837", "Pedro Arthur", "124798", "2017")
x.imprimir()
y = AlunoGraduacao("8649", "Rafael Santos", "103497", "2017/2")
y.imprimir()