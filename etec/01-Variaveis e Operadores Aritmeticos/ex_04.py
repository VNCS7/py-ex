#4.	Crie um algoritmo que receba o nome do aluno e suas 4 notas bimestrais, calcule e apresente a média anual desse aluno.

nome = input('\nDigite o nome do aluno: ')
n1 = float(input('\nDigite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
n3 = float(input('Digite a 3ª nota: '))
n4 = float(input('Digite a 4ª nota: '))

print('\nPrezado(ª)', nome, ', sua média anual é: ', ((n1+n2+n3+n4)/4))
