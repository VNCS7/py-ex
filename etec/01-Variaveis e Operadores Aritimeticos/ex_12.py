#12.	Elabore um programa que calcule o custo para pintar a área de um tanque cilíndrico. Sabendo-se-que:

#• Cada litro de tinta pinta 3 metros;
#• Que cada lata de tinta possui 5 litros;
#• E que cada lata de tinta custa R$120,00.

#Apresentar ao final:
#	Qual o custo total e quantas latas de tintas serão necessárias.

raio = float(input('\nDigite o raio do tanque: '))
altura = float(input('Digite a altura do tanque: '))
area = (2*3.14*raio*(altura + raio))
print('\nCusto Total: ', (area/3)*120, '\nQuantidade de latas: ',area/3)

