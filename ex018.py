import math
a1 = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(a1))
coss = math.cos(math.radians(a1))
tang = math.tan(math.radians(a1))
print(f'O ângulo de {a1} tem o SENO de {seno:.2f}')
print(f'O ângulo de {a1} tem o COSSE de {coss:.2f}')
print(f'O ângulo de {a1} tem o TANGENTE de {tang:.2f}')