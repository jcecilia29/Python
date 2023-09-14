'''Condicionais são importantes para se fazer comparações entre variaveis ou
valores boolenos, numéricos ou de palavras 
Pra realizar esses elementos é necessário utilizar a condição if seguida um senão
else ou nada
'''
moeda= True
ponto= 0
nome= str(input("nome do personagem:\n"))
if((nome== "Mario" and moeda== True) or (nome== "mario" and moeda== True)):
    ponto= ponto +1
    print(f'{nome} pegou a moeda e teve {ponto}')
    moeda= str(input("deseja pegar mais moedas?\n"))
    if(moeda== "sim"):
        ponto= ponto +1
        print(f"{nome} pegou a moeda e teve {ponto}")
    else:
        print(f"não quis pegar mais moedas")
else:
    print("não pegou a moeda")