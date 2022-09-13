# Vamos fazer um programa para verificar quem é o assassino de um crime. Para descobrir o
# assassino, a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser
# sim ou não:
# 1. Mora perto da vítima?
# 2. Já trabalhou com a vítima?
# 3. Telefonou para a vítima?
# 4. Esteve no local do crime?
# 5. Devia para a vítima?
# Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5
# pontos são os assassinos, com 4 a 3 pontos são cúmplices e 2 pontos são apenas suspeitos,
# necessitando de outras investigações. Valores abaixo de 2 são liberados.
# No seu programa, você deve fazer essas perguntas e, de acordo com as respostas do usuário,
# você vai informar como a polícia o considera.


p1 = input('Você mora perto da vítima ? ')
p2 = input('Já trabalho com a vítima ? ')
p3 = input('Telefonou para a vítima ? ') 
p4 = input('Esteve no local do crime ? ')
p5 = input('Devia para a vítima ? ')

cont = 0

if ((p1 == 'Sim') or (p1 == 's')):
    cont+=1

if ((p2 == 'Sim') or (p2 == 's')):
    cont+=1

if ((p3 == 'Sim') or (p3 == 's')):
    cont+=1

if ((p4 == 'Sim') or (p4 == 's')):
    cont+=1

if ((p5 == 'Sim') or (p5 == 's')):
    cont+=1

if (cont == 5):
    print('O suspeito é o assassino !')
elif(3<=cont<=4):
    print('O suspeito é um cumplice.')
elif(cont == 2):
    print('Precisa de mais investigações.')
else:
    print('Liberado.')