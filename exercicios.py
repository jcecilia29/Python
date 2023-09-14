'''
1) Data de nascimento: criar um programa que pergunte ao usuario seu nome
e a data de seu nascimento e calcule a idade com base no ano atual'''
print("exercicio 1")
nome = (input("digite seu nome:"))
dataNascimento = (input("digite sua data de nascimento:"))
x = int(2023)
y = int(2006)
idade = x-y
print(f"calculo da idade é: {idade}")


'''2) Crie um programa em que o usuario digite os valores e o programa calcula
a base de um triangulo retangulo'''
print("exercicio 2")

valores = "digite os valores abaixo"
print(valores)
cateto1 = int(input("valor desejado 1: "))
cateto2 = int(input("valor desejado 2: "))
print(f"hipotenusa: {(cateto1**2+cateto2**2)**0.5}")

'''3) Crie um programa que o usuario digite o peso e altura e o programa calcule o 
IMC indice de massa corporal'''
print("exercicio 3")
peso= float(input("digite o seu peso: "))
altura= float(input("digite a sua altura: "))
print(f"imc:{(peso/(altura**2))}")

'''4) Crie um programa em que o usuario digite um numero em graus celsius e o 
programa converte em farenheint'''
print("exercicio 4")
celsius= float(input("digite o valor de celsius: "))
farenheit= (celsius*9/5)+32
print(f"o valor em farenheit é: {farenheit}")

'''5)Faça o mesmo com farenheint e celsius'''
print("exercicio 5")
farenheit= float(input("digite o valor de farenheit: "))
celsius+ (farenheit-32)*5/9
print(f"o valor de celsius é: {celsius}")

'''6) Crie um programa que calcule baskara dos valores digitados regras a tem que
ser sempre elevado ao quadrado x² mas a pode ter qualquer valor ax² + ou - bx 
ou - c = 0'''
print("exercicio 6")
a= int(input("a: "))
b= int(input("b: "))
c= int(input("c: "))
delta= float(pow(pow(b,2)-4*a*c,1/2))
print(delta)
x1= -b+delta/2*a
x2= -b-delta/2*a
print(f"x1 = {x1:.2f} e x2 = {x2:.2f}")



