import math
from random import choice
a1 = str(input('Primeiro amigo:'))
a2 = str(input('Segundo amigo:'))
a3 = str(input('Terceiro amigo:'))
lista = [a1,a2,a3]
escolhido = choice(lista).upper()
num = float(input(f'Digite um número para calcular o prêmio de {escolhido}:'))
raiz = math.sqrt(num)
premio = math.trunc(raiz)
print('-' * 30)
print(f'O ganhador foi {escolhido}')
print(f'O valor do premio "inteiro" é:{premio}')
print('-' * 30)