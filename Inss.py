# Faça um Programa que pergunte o quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato.

# O programa deve nos informar:

# A. salário bruto.
# B. quanto pagou ao INSS.
# C. quanto pagou ao sindicato.
# D. o salário líquido.

# Calcule os descontos e o salário líquido, conforme a tabela abaixo:

# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

gph = round(float(input('Informe quanto ganha por hora: ')),2)
horas = int(input('Informe quantas horas trabalhou esse mês: '))

total = round((gph * horas),2)
ir = round((total * 0.11),2)
inss = round((total * 0.08),2)
sind = round((total * 0.05),2)

totall = round((total - ir - inss - sind),2)

print('+ Salário Bruto : R$ ' + str(total))
print('- IR (11%) : R$ ' + str(ir))
print('- INSS (8%) : R$ ' + str(inss))
print('# - Sindicato ( 5%) : R$ ' + str(sind))
print('= Salário Liquido : R$ ' + str(totall))
