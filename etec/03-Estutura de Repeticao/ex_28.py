#28.	Crie um algoritmo que controle uma conta poupança que foi aberta com um depósito de R$500,00.
# Sendo a remuneração de 1% ao mês de juros. Apresente o saldo após três meses.

dep=500

for i in range(3):
    dep = dep+(dep*0.01)
print('\nSaldo após 3 meses: {}'.format(dep))

