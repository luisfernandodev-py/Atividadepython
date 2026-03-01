larg= float(input('Qual a largura da parede em metros:'))
alt = float(input('Qual a altura da parede em metros:'))
a = larg  * alt
print(f'Sua parede tem dimensão de {larg} x {alt} e sua área é de {a:.2f}m²')
print(f'para pintar essa parede, você precisará de {a/2:.3f}L de tinta')