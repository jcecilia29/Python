'''Exercicio jo ken po o jogador escolherá pedra papel tesoura e o computador
também atraves de um numero aleatório de 1 a 3
@author alunos de python data: 18/09/2023
version 1.0'''

from random import randint
from time import sleep
print("#"*50)
print("Bem vindo ao jogo de Jo Ken Po 👊✋✌")
sleep(2)
print("👊")
sleep(2)
print("✋")
sleep(2)
print("✌")

escolhaplayer= int(input('''
Digite [1]- 👊
Digite [2]- ✋
Digite [3]- ✌
'''))
print(f"Sua escolha foi {escolhaplayer}")
if(escolhaplayer== 1):
    print(f"A sua escolha foi 👊")
elif(escolhaplayer== 2):
    print(f"A sua escolha foi ✋")
elif(escolhaplayer== 3):
    print(f"A sua escolha foi ✌")
else:
    print("Digite uma opção entre 1 e 3 e reinicie")
escolhacomputador= randint(1,3)
if (escolhacomputador== 1):
    print(f"O computador escolheu: 👊")
elif (escolhacomputador== 2):
    print(f"O computador escolheu: ✋") 
elif (escolhacomputador== 3):
    print(f"O computador escolheu: ✌")
if (escolhaplayer== escolhacomputador):
    print(f"Deu empate")
'''
Pedra ganha de tesoura 1 ganha de 3
Papel ganha de pedra 2 ganha de 1
Tesoura ganha de papel 3 ganha de 2
'''
if((escolhaplayer== 1 and escolhacomputador== 3) or
   (escolhaplayer== 2 and escolhacomputador== 1) or
   (escolhaplayer== 3 and escolhacomputador== 2)):
    print('''Parabéns você é o vencedor!!!😊''')
else:
    print('''Você perdeu playboy, game over😝''')




