#33.	O índice de massa corporal (Peso/Alt²) avalia o nível de gordura de cada pessoa e é adotado pela Organização Mundial da Saúde(OMS).
# O IMC de uma pessoa é dado pela divisão da massa em KG pela altura em metros elevado ao quadrado. Elabore um algoritmo que, a partir da massa
# e da altura informados pelo usuário, calcule e apresente seu IMC de várias pessoas e sua classificação conforme a tabela seguinte:
#• <18 Magreza
#• 18,0 a 24,9 Saudável
#• 25,0 a 29,7 Sobrepeso
#• >= 30,0 Obesidade
sair = ""

while(sair!="S"):

    kg = float(input("\nDigite seu peso: "))
    al = float(input("Digite sua altura: "))
    imc = kg/(al**2)

    if imc<18:
        print("\nMagreza\m")
    elif imc >= 18 and imc <=24.9:
        print("\nSaudável\n")
    elif imc >= 25 and imc<=29.7:
        print("\nSobrepseo\n")
    elif imc >= 30:
        print("\nObesidade\n")

    sair = input('Deseja sair? S = SIM | N = NÃO \n\t -> ')