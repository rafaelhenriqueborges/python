# Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
# • Para homens: (72.7h) - 58
# • Para mulheres: (62.1h) - 44.7

sexo = input('Informe seu sexo. M para masculino e F para feminino: ') 
altura = float(input('Informe sua altura: '))

if (sexo == 'M'):
    p = (72.2 * altura) - 58
    peso = round(p,2)
    print(peso)
else:
    p = (62.1 * altura) - 44.7
    peso = round(p,2)
    print(peso)