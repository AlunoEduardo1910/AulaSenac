produtos = {"Ovo de páscoa" : 1000, "café": 100, "cenoura" : 2.5, "Pacote de chá": 0.99, "Mouse Gamer Pro 2030" : 150}
for produto,  preco in produtos.items():
    if preco > 20:
        print(f'O produto {produto} custa o total de {preco}')
