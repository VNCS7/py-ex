#19.	Crie um algoritimo que receba o ano de nascimento de uma pessoa. Calcule e mostre se atingiu a maioridade ou não.

nasc = float(input("\nDigite o ano de nascimento: "))
ano =  float(input("Digite o ano atual: "))
id = ano-nasc

if id >=18:
    print("\nVocê tem", id, "anos e atingiu a maioridade")
else:
    print("\nVocê tem", id, "anos e ainda não atingiu a maioridade")