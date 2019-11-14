lista_produto=[]
lista_quantidade=[]
lista_preco=[]
contador=0
acumulador=0


i=input('Tem produtos no carrinho? [S/N] ').upper()
while i=="S":
    
    produto = input("Nome do produto: ").upper()
    lista_produto.append(produto)
    quantidade = int(input('Quantidade do mesmo produto: '))
    lista_quantidade.append(quantidade)
    preco = float(input("Preço unitario do produto: "))
    lista_preco.append(preco)
    i=input('Tem produtos no carrinho? [S/N] ').upper()

print("Lista da compra")    

while   contador<len(lista_produto) :
    

   print(lista_produto[contador],' x ',lista_quantidade[contador],' Preço unitario R$',lista_preco[contador],' Preço total R$',(lista_quantidade[contador]*lista_preco[contador]))
   acumulador += lista_preco[contador]*lista_quantidade[contador]
   contador=contador+1
print('Total da sua compra R$',acumulador)

