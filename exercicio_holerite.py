salario=int(input("digite seu salario "))
inss=salario*9/100
vt=salario*3/100
valor_integral_do_plano_de_saude=347
plano_saude=valor_integral_do_plano_de_saude*15/100

print("seu salario integral é ",salario)
print("seu salario descontado o inss é ",salario-inss)
print("seu salario descontado o vale transporte é ",salario-vt)
print("seu salario descontado o plano de saúde é ",salario-plano_saude)
print("seu salario liquido é ",salario-inss-vt-plano_saude)
