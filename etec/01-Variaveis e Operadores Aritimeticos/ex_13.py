#13.	Elabore um programa que leia dois valores inteiros (A e B), e ao final do processamento apresente os valores trocados.

a = int(input('\nDigite o valor de A: '))
b = int(input('Digite o valor de B: '))
x = 0

x = a
a = b
b = x

print('\nA: ', a, '\nB: ', b)