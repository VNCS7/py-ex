#27.	Crie um programa que receba 3 valores A,B e C. Supondo que cada valor seja um dos lados de um triângulo,
# verifique e informe se estes lados compõem um triângulo equilátero, isósceles ou escaleno,
# informar se não compõem um triângulo.

a = float(input("\nDigite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

if a+b >= c or a+c >= b or b+c >= a:
    if a == b and b == c:
        print("\nValores inseridos formam um triângulo Equilátero.")
    elif a == b and c !=b or a == c and a != b or b == c and a != c:
        print("\nValores inseridos formam um triângulo Isósceles.")
    elif a != b and b != c:
        print("\nValores inseridos formam um triângulo Escaleno")
else:
    print("\nValores inseridos não formam um triângulo!")
