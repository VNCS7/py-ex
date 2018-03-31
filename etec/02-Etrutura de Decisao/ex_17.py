#17.	Crie um algoritmo que calcule a multa paga por um pescador que ultrapassar a quantidade de quilos estabelecida por lei.
#  A saber:
#• A quantidade de peixe por pessoa é 50 kg;
#• A multa por quilo excedente é R$4,00.

qt_p = float(input("\nDigite a quantidade de KG pescado: "))

if qt_p >50:
    print("\nMulta a ser paga será de R$: ", (qt_p-50)*4.00)

else:
    print("\nQuantidade está dentro do padrão, multa não aplicada")