# Algoritmo que recebe um valor e imprime a sua tabuada.

num = int(input('Digite um número: '))
for i in range (1,11):
    tab = num * i
    print(tab, end =' ')