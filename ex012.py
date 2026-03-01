preco = float(input('Qual é o preço do produto?'))
desc = (preco * 5) / 100
print(f'O produto que costava R${preco:.2f}, na promoção de 5% vai custar R${preco-desc:.2f} ')