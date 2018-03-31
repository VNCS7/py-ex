#11.	Crie um algoritmo que calcule e apresente a área externa de uma lata,
# onde é fornecido pelo usuário somente o Raio e a Altura.

raio = float(input('\nDigite o raio da lata: '))
altura = float(input('Digite a altura da lata: '))
print('\nÁrea da lata = ',2*3.14*raio*(altura + raio))