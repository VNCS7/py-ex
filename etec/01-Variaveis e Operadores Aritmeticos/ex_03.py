#3.	Crie um algoritmo que receba o ano de nascimento de uma pessoa,
# calcule e mostre e a idade atual e quantos anos a pessoa terá em 2050.

dt_nas = int(input('Em que ano você nasceu?    \n-> '))
ano_atual = int(input('Em que ano estamos?  \n-> '))

print('\nAtualmente você tem', ano_atual-dt_nas, 'anos ', '\nEm 2050, você terá', 2050-dt_nas, 'anos')
