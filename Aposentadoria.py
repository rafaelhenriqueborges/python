
# Suponha que uma pessoa possa se aposentar pelo INSS caso atenda alguma das situações abaixo: 
# • É do gênero masculino, possui pelo menos 65 anos e pelo menos 10 anos de contribuição.
# • É do gênero masculino, possui pelo menos 63 anos e pelo menos 15 anos de contribuição.
# • É do gênero feminino, possui pelo menos 63 anos e pelo menos 10 anos de contribuição. 
# • É do gênero feminino, possui pelo menos 61 anos e pelo menos 15 anos de contribuição. 
# Crie um programa que leia um caractere (‘M’ ou ‘F’), que representa o gênero de um indivíduo, 
# e dois inteiros, que representam a idade e o tempo de contribuição. O programa deverá então imprimir “Aposentável” 
# se o indivíduo atender uma das situações acima. Caso contrário, o programa deverá imprimir “Não Aposentável”.


sexo = input('Informe o seu sexo. M para masculino e F para feminino: ') 
idade = int(input('Informe sua idade: '))
contri = int(input('Informe seu tempo de contribuição: '))

if (sexo == 'M' ):
    if ((idade >= 65 and contri >= 10) or (idade >= 63 and contri >= 15)):
        print('Aposentável')
    else:
        print('Não Aposentável')
else:
    if ((idade >= 65 and contri >= 10) or (idade >= 63 and contri >= 15)):
        print('Aposentável')
    else:
        print('Não Aposentável')