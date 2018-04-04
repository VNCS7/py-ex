#31.	Tendo como dados de entrada a altura e o sexo de 15 Pessoas, construa um algoritmo que calcule o peso ideal, utilizando as seguintes fórmulas:
#Homem=(72.7*ALT)-58;
#$Mulher=(62.1*ALT)-44.7.
pessoa=1
while(pessoa<=15):

    al = float(input("\nDigite sua altura: "))
    sx = input("Digite seu sexo: (M = Masculino | F = Feminino)\n\t-> ")

    if sx == "M":
        print("\nPessoa {}:\nPeso ideal é: {}".format(pessoa,((72.7*al)-58)))
    else:
        print("\nPessoa {}:\nPeso ideal é: ".format(pessoa,(((62.1 * al) - 44.7))))

pessoa+=1