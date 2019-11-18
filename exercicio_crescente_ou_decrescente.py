lista_numero=[10,2,5,8,100,0,65,7,6,1,94,37]
decisao=int(input("Digite 1 para ordenar de forma Crescente ou 2 para Decrescente "))
if decisao==1:
    print(sorted(lista_numero,reverse=0))
elif decisao==2:
    print(sorted(lista_numero,reverse=1))
else:
    print("Opção invalida")