#18.	Crie um algoritmo que receba uma senha e verifique sua validade ou não. Senha válida “asdfg”.

senha = input("\nDigite a senha: ")

if senha == "asdfg":
    print("\n\t-> Acesso Liberado!")
else:
    print("\n\t-> Senha Incorreta, Acesso Negado!")