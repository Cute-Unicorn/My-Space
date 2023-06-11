"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

nmr = input('Digite um número inteiro: ')
try:
    nmr_int = int(nmr)
    if (nmr_int % 2) == 0:
        print('Este número é par')
    else:
        print('Este número é ímpar')
except:
    print('O número informado não é um inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite o horário (0 a 23): ')
try:
    hora_int = int(hora)
    if (hora_int >= 0) and (hora_int <= 11):
        print('Bom dia')
    elif (hora_int >= 12) and (hora_int <= 17):
        print('Boa tarde')
    else:
        print('Boa noite')
except:
    print('O número informado não corresponde a um horário')

"""
Faça um programa que peça o nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite seu nome: ')
if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) == 5 or len(nome) == 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
