nome=input("nome do produto ")
preco=float(input("preço do produto "))
quantidade=int(input("quantidade "))
print(quantidade, nome, "R$",quantidade*preco)
s=input("tem mais mercadoria no carrinho [s/n]")

while s=="s":
 nome=input("nome do produto ")
 preco=float(input("preço do produto "))
 quantidade=int(input("quantidade "))
 print(quantidade, nome, "R$",quantidade*preco)
 s=input("tem mais mercadoria no carrinho [s/n]")
print("fim")
