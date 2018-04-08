#44.	Crie um  programa que classifique os nadadores nas categorias de acordo com sua idade:
#Infantil A – de 5 à 7 anos;
#Infantil B – de 8 à 10 anos;
#Juvenil A – de 11 à  13 anos;
#Juvenil B  - de 14 à 17 anos;
#Senior – a partir de 18 anos.

nadador = 1
while(nadador <=5):
    nadador+=1
    id = int(input("\nDigite a idade: "))

    if id >= 5 and id <= 7:
        print("\nCategoria: Infantil A")
    elif id >= 8 and id <= 10:
        print("\nCategoria: Infantil B")
    elif id >= 11 and id <= 13:
        print("\nCategoria: Juvenil A")
    elif id >= 14 and id <= 17:
        print("\nCategoria: Juvenil B")
    elif id >= 18:
        print("\nCategoria: Senior")
