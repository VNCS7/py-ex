#39.	Escrever um programa para apresentar o nome do lanche do MacDonalds conforme no nº da opção digita pelo cliente (usuário):
#• 1.BigMac
#• 2.Quarteirão
#• 3.MacChicken
#• 4. Cheddar MacMelt
#• 5. MacMax

encerrar =''
while(encerrar !='S'):

    print("\nSelecione um dos lanches abaixo:"+"\n1.BigMac"+"\n2.Quarteirão"+"\n3.MacChicken"+"\n4. Cheddar MacMelt"+"\n5. MacMax")
    op = int(input("\nDigite sua escolha: "))

    if op ==1:
        print("\nBigMac")
    elif op==2:
        print("\nQuarteirão")
    elif op==3:
        print("\nMacChicken")
    elif op==4:
        print("\nCheddar MacMelt")
    elif op==5:
        print("\nMacMax")
    else:
        print("\nOPÇÃO INVÁLIDA")

    encerrar=input('\nDeseja encerrar o pedido ? S= SIM | N=Não \n\t-> ')