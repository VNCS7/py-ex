#32.	Crie um algoritmo que receba uma senha e verifique sua validade ou não. Senha válida “asdfg”.
# Se o usuário digitar errado mais de 3 vezes finalizar o programa.
error=1
senha=""

while(senha!="asdfg"):
    senha = input(('\nInsira a senha: '))

    if error >=3:
        print('\nNúmero máximo de tentativas excedido, encerrando...')
        break
    if (senha!="asdfg"):
        error+=1
    else:
        print('\nAcesso concedido!')
        break
