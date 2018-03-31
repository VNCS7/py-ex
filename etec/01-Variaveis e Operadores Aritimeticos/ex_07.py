#7.	 Elabore um algoritmo que leia uma medida em centímetros e apresente quantos metros, decímetros e milímetros
# há nesta medida.

medida = float(input('\nDigite uma medida em centímetros: '))
print('\n', medida, ' centímetros em metros:     ',medida*0.01, '\n', medida, ' centímetros em decímetros: ', medida*0.1, '\n', medida, ' centímetros em milímetros: ', medida*10)