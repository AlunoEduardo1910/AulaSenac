try:
    codigo = int(input("Digite um código de produto de 1 à 5: "))

    match codigo:
        case 1:
            print(f'{codigo} = Eletrônicos')
        case 2:
            print(f'{codigo} = Roupas')
        case 3:
            print(f'{codigo} = Alimentos')
        case 4:
            print(f'{codigo} = Livros')
        case 5:
            print(f'{codigo} = Brinquedos')
        case _:
            print("Código inválido")
except:
    print("Número inválido")