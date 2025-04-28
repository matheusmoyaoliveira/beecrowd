# 🧪 Quando usar map()?
# Sempre que você quiser aplicar a mesma transformação em vários itens de uma vez:

# Converter tudo pra INT

# Converter tudo pra FLOAT

# Colocar tudo em STR

# Etc.

pi = 3.14159

a, b, c = map(float, input().split())

areat = (a * c) / 2
areac = pi * (c ** 2)
areatr = (a + b) * c / 2
areaq = b * b
arear = a * b

print('TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3F}'.format(areat, areac, areatr, areaq, arear))