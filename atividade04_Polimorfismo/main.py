############################################# Objeto Veículo ############################################
class Veiculo:
    def __init__(self, marca, qtd_rodas, modelo, velocidade_atual):
        self.marca = marca #string
        self.qtd_rodas = qtd_rodas #int
        self.modelo = modelo #string
        self.velocidade_atual = velocidade_atual #int = 0

    def imprimir_veiculo(self):
        print("Marca:", self.marca)
        print("Quantidade de rodas:", self.qtd_rodas)
        print("Modelo:", self.modelo)
        print("Velocidade atual:", self.velocidade_atual)

    def acelerar(self, velocidade_atual):
        self.acelerar += velocidade_atual

    def frear(self, velocidade_atual):
        self.frear -= velocidade_atual

########################################### Objeto Automóvel ###########################################
class Automovel(Veiculo):
    def __init__(self, marca, qtd_rodas, modelo, velocidade_atual, potencia_motor):
        super(Automovel, self).__init__(marca, qtd_rodas, modelo, velocidade_atual)
        self.potencia_motor = potencia_motor #double

    def imprimir_automovel(self):
        Veiculo.imprimir_veiculo(self)
        print("Potência do motor:", self.potencia_motor, "cv")

############################################## Objeto Carro #############################################
class Carro(Automovel):
    def __init__(self, marca, qtd_rodas, modelo, velocidade_atual, potencia_motor, qtd_portas):
        super(Carro, self).__init__(marca, qtd_rodas, modelo, velocidade_atual, potencia_motor)
        self.qtd_portas = qtd_portas #int

    def imprimir_carro(self):
        Automovel.imprimir_automovel(self)
        print("Quantidade de portas:", self.qtd_portas)

############################################## Objeto Moto ##############################################
class Moto(Automovel):
    def __init__(self, marca, qtd_rodas, modelo, velocidade_atual, potencia_motor, partida_eletrica):
        super(Moto, self).__init__(marca, qtd_rodas, modelo, velocidade_atual, potencia_motor)
        self.partida_eletrica = partida_eletrica #boolean

    def imprimir_moto(self):
        Automovel.imprimir_automovel(self)
        print("Partida Elétrica:", self.partida_eletrica)

############################################ Objeto Bicicleta ###########################################
class Bicicleta(Veiculo):
    def __init__(self, marca, qtd_rodas, modelo, velocidade_atual, num_marchas, bagageiro):
        super(Bicicleta, self).__init__(marca, qtd_rodas, modelo, velocidade_atual)
        self.num_marchas = num_marchas #int
        self.bagageiro = bagageiro #boolean

    def imprimir_bicicleta(self):
        Veiculo.imprimir_veiculo(self)
        print("Número de marchas:", self.num_marchas)
        print("Bagageiro:", self.bagageiro)

################################################ Running ###############################################
print("(Atividade 04 - Polimorfismo)")
print("=============================")
v = Veiculo("McLaren", 4, "P13", "250 km/h")
v.imprimir_veiculo()
print("=============================")
a = Automovel("Koenigsegg", 4, "One:1", "395 km/h", 1140)
a.imprimir_automovel()
print("=============================")
c = Carro("Volkswagen", 4, "Golf GTI 2021", "120 km/h", 245, 4)
c.imprimir_carro()
print("=============================")
m = Moto("Kawazaki", 2, "z1000", "200 km/h", 138, True)
m.imprimir_moto()
print("=============================")
b = Bicicleta("Caloi", 2, "Sport Comfort", "25 km/h", 21, False)
b.imprimir_bicicleta()
print("=============================")