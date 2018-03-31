#5.	Crie um algoritmo que calcule o salário líquido sabendo que:
# A cada um dependente, este recebe R$ 300,00 de bônus.
# O valor do seu salário bruto é: Valor Hora * Horas Trabalhadas no Mês.
# A aplicação irá coletar o número de dependentes, valor hora, horas trabalhadas
#  e apresentará o valor bruto e o valor líquido.

n_dep = int(input('\nDigite a quantidade de dependentes: '))
vl_hr = float(input('Digite o valor da hora trabalhada: '))
hr_tr = float(input('Digite a quantidade de horas trabalhadas: '))

print('\nSalário bruto: R$', vl_hr*hr_tr, '\nSalário líquido: R$', (vl_hr*hr_tr)+n_dep*300.00)