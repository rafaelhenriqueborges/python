# Crie uma função que recebe o valor do raio de um círculo como parâmetro e retorna o valor da
# área desse círculo. Lembrando que a área de círculo é dada pela equação: A = ℼ r^2.

import math

raio = round(float(input('Informe o raio do círculo: ')),2)

area = round((math.pi * (raio ** 2)),2)

print(area)