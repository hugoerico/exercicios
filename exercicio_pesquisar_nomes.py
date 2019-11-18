lista_nomes=['amanda','beatriz','hugo','barbara','vanessa','fernanda','erico']
pesquisa=input('digite a inicial do nome para pesquisa ')

parar = False
for nomes in lista_nomes:
        if nomes[0]==pesquisa:
            print(nomes)
        
            break
        else:
            print('Não tem nomes iniciados com ',pesquisa)
            break

   
    
    