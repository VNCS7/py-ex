#40.	Refaça o algoritmo para calcular 5 equações do 2º grau, levando em consideração a análise da existência do X1 e X2 .

equacao =1

while(equacao<=5):
    equacao+=1
    a = float(input('\nDigite o valor de A: '))
    b = float(input('Digite o valor de B: '))
    c = float(input('Digite o valor de C: '))

    delta = (pow(b, 2)) - (4 * a * c);
    x1 = (-b + delta ** (1.0 / 2.0)) / (2.0 * a)
    x2 = (-b - delta ** (1.0 / 2.0)) / (2.0 * a)

    if delta <= 0:
        print("\nErro: Delta Menor/Igual a 0, equação não pôde ser continuada!")
    else:
        print('\nX1 =  ', x1, '\nX2 = ', x2)
