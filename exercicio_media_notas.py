nota1=int(input('primeira nota '))
nota2=int(input('segunda nota '))
nota3=int(input('terceira nota '))
nota4=int(input('quarta nota '))
nota_final= (nota1+nota2+nota3+nota4)/4
if(nota_final>=7):
  print('aluno aprovado com média ',nota_final)
elif(nota_final>=5.5):
  print('aluno em recuperação com média ',nota_final ) 
else:
  print('aluno reprovado com média ',nota_final)   


# com while

lista=[]
i=0
j=0
acumulador=0
while i<4:
    i+=1
    nota_inserida = float(input("entre com a nota " + str(i)+ 'do aluno: '))
    lista.append(nota_inserida)

while j<4:
    acumulador += lista[j]
    j+=1

media = acumulador/4
if(media>=7):
  print('aluno aprovado com média ',media)
elif(media>=5.5):
  print('aluno em recuperação com média ',media )
else:
  print('aluno reprovado com média ',media)
