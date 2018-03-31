#16.	Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes formulas:
#•Homem=(72.7*ALT)-58;
#•Mulher=(62.1*ALT)-44.7;

al = float(input("\nDigite sua altura: "))
sx = input("Digite seu sexo: (M = Masculino | F = Feminino)\n\t-> ")

if sx == "M":
    print("\nPeso ideal é: ", (72.7*al)-58)
else:
    print("\nPeso ideal é: ", (62.1 * al) - 44.7)
