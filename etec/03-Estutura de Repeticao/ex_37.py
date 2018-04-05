#37.	Elabore um algoritmo que leia 10 medidas diferentes em centímetros e apresente quantos metros,
# decímetros e milímetros há nesta medida.

medidas = 1

while(medidas<=10):
    medidas += 1
    medida = float(input('\nDigite uma medida em centímetros: '))
    print('\n', medida, ' centímetros em metros:     ', medida * 0.01, '\n', medida, ' centímetros em decímetros: ',
          medida * 0.1, '\n', medida, ' centímetros em milímetros: ', medida * 10)
