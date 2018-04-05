#35.	Crie um algoritmo para calcular a área de 8 triângulos, apresente cada resultado.

triangulo = 1

while(triangulo<=8):
    base=float(input('\nDigite a base do triângulo: '))
    altura=float(input('Digite a altura do triângulo: '))
    triangulo+=1
    print('\nÁrea do triângulo é igual a {}'.format((base*altura)/2))