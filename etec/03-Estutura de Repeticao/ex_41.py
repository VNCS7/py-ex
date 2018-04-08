# 41.	Faça um algoritmo para calcular o volume de 10 esferas de raio R, em que R é um valor fornecido pelo usuário.

esfera = 1
while(esfera<=10):
    esfera +=1
    raio = float(input('\nDigite o valor do raio: '))
    print('\nVolume da esfera de Raio', raio, ' = ', 4 * 3.14 * raio ** 3 / 3)