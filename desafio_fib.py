l = int(input('Quer ver a sequêcia até qual valor?'))
a = 0
b = 1
while b < l:
    print(b,end='->')
    a,b = b,a+b
print()
print('FIM')