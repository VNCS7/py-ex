#21.	O índice de massa corporal (Peso/Alt²) avalia o nível de gordura de cada pessoa e é adotado pela
# Organização Mundial da Saúde(OMS). O IMC de uma pessoa é dado pela divisão da massa em KG pela altura em
# metros elevado ao quadrado. Elabore um algoritmo que, a partir da massa e da altura informados pelo usuário,
# calcule e apresente seu IMC e sua classificação conforme a tabela seguinte:
#• <18 Magreza
#• 18,0 a 24,9 Saudável
#• 25,0 a 29,7 Sobrepeso
#• >= 30,0 Obesidade

kg = float(input("\nDigite seu peso: "))
al = float(input("Digite sua altura: "))
imc = kg/(al**2)

if imc<18:
    print("\nMagreza")
elif imc >= 18 and imc <=24.9:
    print("\nSaudável")
elif imc >= 25 and imc<=29.7:
    print("\nSobrepseo")
elif imc >= 30:
    print("\nObesidade")