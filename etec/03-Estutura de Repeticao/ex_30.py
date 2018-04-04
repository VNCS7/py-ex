#30.	Crie um algoritmo que receba 4 notas bimestrais, de 7 alunos diferentes, calcule e apresente a média anual de cada aluno.
aluno=1
nota = [5]
while(aluno <=7):

    n1 = float(input('\nDigite a 1ª nota: '))
    n2 = float(input('Digite a 2ª nota: '))
    n3 = float(input('Digite a 3ª nota: '))
    n4 = float(input('Digite a 4ª nota: '))

    print('\nMédia do aluno {} é: {}'.format(aluno,(n1+n2+n3+n4)/4))

    aluno+=1