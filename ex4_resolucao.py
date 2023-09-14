from datetime import date
diaatual= date.today().day
mesatual= date.today().month
anoatual= date.today().year
print(f"{diaatual}/{mesatual}/{anoatual}")
dianascimento= int(input("Dia do nascimento: "))
mesnascimento= int(input("Dia do nacsimneto: "))
anonascimento= int(input("Dia do nascimento: "))
dataatual= (f"{diaatual}/{mesatual}/{anoatual}")
print(f"{dianascimento}/{mesnascimento}/{anonascimento}")
dataaniversario= (f"{dianascimento}/{mesnascimento}/{anonascimento}")
idade= anoatual-anonascimento
print(f"idade: {idade}")
datadeaniversario= (f"{dianascimento}/{mesnascimento}/{anonascimento}")
idade= (anoatual-anonascimento)
if (anonascimento==anoatual):
    print("Feliz Aniversario!")
else:
    print("Aguarde seu aniversário")