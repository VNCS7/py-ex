#29.	Desenvolva um algoritmo que receba a base e altura de um retângulo, calcule e mostre sua área, repita 10 com valores diferentes.
retangulo =1
while(retangulo <=10):
    base = float(input('\nDigire a base do retângulo: '))
    altura = float(input('Digite a altura do retângulo: '))
    print('\nÁrea de um retângulo de base {} e altura {} é igual a: {}'.format(base,altura,base*altura))
    retangulo+=1