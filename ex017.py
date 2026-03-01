from math import hypot
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjacente:'))
hi = hypot(co,ca)
print(f'A hipotenusa vai medir { hi:.1f}')
co2 = float(input('Digite o valor do cateto oposto:'))
ca2 = float(input('Digite o valor do cateto adjacente:'))
hi2 = (co2**2 + ca2**2)**(1/2)
print(f'A hipotenusa vai medir {hi2:.1f}')