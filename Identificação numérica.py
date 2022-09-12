# Considere um programa que deve classificar um número como par ou ímpar e, além disso, 
# classificar ele como menor do que 100 ou maior ou igual a 100. 
# Escreva um programa que faça essa classificação corretamente.


num = int(input('Insira um número inteiro: '))

if (num % 2 == 0):
    if (num < 100):
        print('Número par e menor que 100.')
    elif (num == 100):
        print('Número par e igual a 100.')
    else:
        print('Número par e maior que 100.')
else:
    if (num < 100):
        print('Número impar e menor que 100.')
    else:
        print('Número impar e maior que 100.')    
