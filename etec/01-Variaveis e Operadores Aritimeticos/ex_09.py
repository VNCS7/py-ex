#9.	Construa um algoritmo para calcular e apresentar X¹ e X²
#  da equação do 2ºgrau, sendo que os valores de A, B e C são fornecidos pelo usuário

a = float(input('\nDigite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

delta = (pow(b, 2)) - (4 * a * c);
x1 = (-b+ delta**(1.0/2.0)) / (2.0*a)
x2 = (-b- delta**(1.0/2.0)) / (2.0*a)

print('\nX1 =  ', x1, '\nX2 = ', x2)
