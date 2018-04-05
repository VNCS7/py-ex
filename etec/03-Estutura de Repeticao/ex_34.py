#34.	Crie um algoritimo que calcule o salário líquido de 10 funcionário sabendo que: A cada um dependente, este recebe R$ 300,00 de bônus;
# O valor do seu salário bruto é: Valor Hora * Horas Trabalhadas no mês;
# A aplicação irá coletar o número de Dependentes, Valor Hora, Hora Trabalhada e apresentará o Valor Bruto e Valor Líquido.

funcionario = 1

while(funcionario <=10):
    funcionario +=1
    n_dep = int(input('\nDigite a quantidade de dependentes: '))
    vl_hr = float(input('Digite o valor da hora trabalhada: '))
    hr_tr = float(input('Digite a quantidade de horas trabalhadas: '))
    print('\nSalário bruto: R$', vl_hr*hr_tr, '\nSalário líquido: R$', (vl_hr*hr_tr)+n_dep*300.00)