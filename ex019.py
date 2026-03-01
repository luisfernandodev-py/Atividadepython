import random
n1 = str(input('Primeriro aluno: '))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno'))
n4 = str(input('quarto aluno'))
lista = [n1,n2,n3,n4]
escolhido =random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')