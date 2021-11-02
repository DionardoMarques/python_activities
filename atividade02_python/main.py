produtos = ["mouse" , "teclado" , "headset"]
preco = [150.0 , 260.0 , 350.99]
quantidade_prod = [120 , 80 , 52]

#func para printar um dos itens da lista
def listar_produto():
    print((produtos[2]))
#func para retirar um dos itens da lista
def remove_produto():
    produtos.remove("mouse")
#running
print(produtos)
listar_produto()
remove_produto()
print(produtos)

print("------------ FIM ------------")