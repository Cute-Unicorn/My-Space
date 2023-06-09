nome = "Lithirias"
altura = 1.64
peso = 64
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.3f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

# Jubileu tem x.xx de altura,
# pesa xx quilos e seu IMC é
# ...

print(linha_1)
print(linha_2)
print(linha_3)
