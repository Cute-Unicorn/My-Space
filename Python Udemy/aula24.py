# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 6 7
#  V i n í c i u s
# -8-7-6-5-4-3-2-1

# nome = 'Vinícius'

# print(nome[2])
# print(nome[-6])

# Procura se o caracter está na variável
# print('n' in nome)
# print('Vin' in nome)
# print('Vin' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')