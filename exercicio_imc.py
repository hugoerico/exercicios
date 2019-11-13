peso=float(input("qual é o seu peso "))
altura=float(input("qual é a sua altura " ))
imc=peso/(altura*altura)
if(imc<18.5):
  print('você está abaixo do peso ideal seu IMC é ',round(imc,2))
elif(imc<=24.9):
  print('parabens você está em seu peso ideal seu IMC é ',round(imc,2))
elif(imc<=30):
  print('você está acima de seu peso (sobrepeso) seu IMC é ',round(imc,2))    
else:
  print('você está obeso seu IMC é ',round(imc,2))
