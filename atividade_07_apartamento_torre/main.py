#Arquivo principal
from Torre import Torre
from Apartamento import Apartamento
from Fila import Fila

#Criando a torre
torre1 = Torre()
torre1.cadastrar(1, "Jussara", "Bloco C")
torre1.imprimir()

print()

#Criando o primeiro apartamento
apto1 = Apartamento()
apto1.cadastrar(40, 205, 46, torre1)
apto1.imprimir()

fila = Fila()

fila.adicionar(apto1)
fila.imprimir()

print()

#Criando o segundo apartamento
apto2 = Apartamento()
apto2.cadastrar(80, 305, 89, torre1)

fila.adicionar(apto2)
fila.imprimir()

fila.remover()
fila.imprimir()