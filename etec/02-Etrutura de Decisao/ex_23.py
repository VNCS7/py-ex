#23.	Crie um algoritmo que receba um número entre 1 e 12  e apresente o  mês correspondente.

#NÃO EXISTE UM 'SWITCH' EM PYTHON, USEI UM DICIONÁRIO PARA 'SIMULAR' UM
# DOCUMENTÇÃO DICIONÁRIOS: https://docs.python.org/3/library/stdtypes.html?highlight=dict#dict

meses = {1:"Janeiro",
         2:"Fevereiro",
         3:"Março",
         4:"Abril",
         5:"Maio",
         6:"Junho",
         7:"Julho",
         8:"Agosto",
         9:"Setembro",
         10:"Outubro",
         11:"Novembro",
         12:"Dezembro"
         }
op = int(input("\nDigite um número de 1 à 12: "))

if op>12:
    print("\nERRO!, SOMENTE NÚMEROS DE 1 À 12")
else:
    print("\nNúmero digitado corresponde ao mês de: ", meses[op])