#36.	Crie um algoritmo que receba o ano de nascimento de 15 pessoas. Calcule e mostre se atingiu a maioridade ou não.

pessoa =1

while(pessoa<=15):

    nasc = float(input("\nDigite o ano de nascimento: "))
    ano =  float(input("Digite o ano atual: "))
    id = ano-nasc
    pessoa += 1
    if id >=18:
        print("\nVocê tem", id, "anos e atingiu a maioridade")
    else:
        print("\nVocê tem", id, "anos e ainda não atingiu a maioridade")