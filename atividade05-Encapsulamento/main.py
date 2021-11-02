######################################################### Objeto Pessoa #######################################################
class Pessoa:
    def __init__(self,codigo, nome, endereco, telefone):
        self.__codigo = codigo
        self.nome = nome
        self._endereco = endereco
        self.__telefone = telefone

    def imprime_nome(self):
        print("Nome: ", self.nome)

    def __imprime_telefone(self):
        print("Telefone: ", self.__telefone)

##################################################### Objeto Pessoa Física ###################################################
class Fisica:
    def __init__(self, codigo, nome, endereco, telefone, cpf, idade, peso, altura):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def imprime_CPF(self):
        print("CPF: ", self.__cpf)

    def __calcula_IMC(self):
        print("Seu IMC: ", self.peso / (self.altura * self.altura), "e sua idade é:", self.idade, "anos")

################################################### Objeto Pessoa Jurídica ##################################################
class Juridica:
    def __init__(self, codigo, nome, endereco, telefone, CNPJ, inscricao_estadual, quantidade_funcionario):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__CNPJ = CNPJ
        self.__inscricao_estadual = inscricao_estadual
        self.quantidade_funcionario = quantidade_funcionario

    def imprime_CNPJ(self):
        print("CNPJ: ", self.__CNPJ)

    def __emitir_nota_fiscal(self):
        print("Nota fiscal nº849201392 para a empresa com os seguintes dados:", self.__CNPJ, "e", self.__inscricao_estadual)

########################################################### Running #########################################################
print("(Atividade 05 - Encapsulamento)")
print("=============================")
p = Pessoa(829301, "Pedro Arthur", "Av.Guilherme Alves, 920", "(51)98204-1282")
p.imprime_nome()
p._Pessoa__imprime_telefone()
print("=============================")
f = Fisica(829301, "Pedro Arthur", "Av.Guilherme Alves, 920", "(51)98204-1282", "080.430.500-67", 21, 80.0, 1.88)
f.imprime_CPF()
f._Fisica__calcula_IMC()
print("=============================")
j = Juridica(829301, "Pedro Arthur", "Av.Guilherme Alves, 920", "(51)98204-1282", "18.236.120/0001-58", "88448866-88", 1500)
j.imprime_CNPJ()
j._Juridica__emitir_nota_fiscal()