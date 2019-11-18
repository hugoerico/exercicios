from random import randint

numero = randint(0,100)

#print(numero)

alternativa = int(input("Digite um número "))
while (alternativa !=numero):  
    
    if alternativa > numero:
        print("o número que você escolheu é maior que o sorteado!")
        alternativa = int(input("Digite um número "))
    print ("o número que você escolheu é menor que o sorteado!")
    alternativa = int(input("Digite um número "))
print("Parabéns você acertou!")    