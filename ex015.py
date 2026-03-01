dia = int(input('Quantos dias alugados?'))
km = float(input('Quantos km rodados? km:'))
alug = (dia * 60) + (km * 0.15)
print(f'O total a pagar é R${alug:.2f}')