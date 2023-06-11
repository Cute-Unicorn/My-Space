primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if(primeiro_valor > segundo_valor):
    texto = f'{primeiro_valor=} é maior do que {segundo_valor=}'
elif(segundo_valor > primeiro_valor):
    texto = f'{segundo_valor=} é maior do que {primeiro_valor=}'
else:
    texto = f'{primeiro_valor=} é igual ao {segundo_valor=}'

print(texto)