# Faça um programa que peça ao usuário um número e imprima todos os números de um até o
# número que o usuário informar.

num = int(input('Informe um número inteiro: '))

for i in range (1, num + 1):
    print(i, end = ' ')