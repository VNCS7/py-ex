#24.Crie um algoritmo que receba 4 notas do aluno e verifique se o mesmo foi aprovado ou reprovado com um dos seguintes conceitos:
#Aprovado:
#A – maior igual à 9
#B – maior igual à 7 e menor que 9
#C – maior igual à 5 e menor que 7

#Reprovado:
#D – maior igual à 2,5 e menor que 5
#E – menor que 2,5

n1 = float(input("\nDigite a 1ª Nota: "))
n2 = float(input("Digite a 2ª Nota: "))
n3 = float(input("Digite a 3ª Nota: "))
n4 = float(input("Digite a 4ª Nota: "))

md = (n1+n2+n3+n4)/4

if md>=9:
    print("\nAprovado - Conceito: A")
elif md>=7 and md <9:
    print("\nAprovado - Conceito: B")
elif md>=5 and md<7:
    print("\nAprovado - Conceito: C")
elif md>=2.5 and md<5:
    print("\nReprovado - Conceito: D")
elif md<2.5:
    print("\nReprovado - Conceito: E")