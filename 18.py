lista = []

while True:
    numero_int = int(input("Digite um número:"))
    if numero_int % 2 == 0:
        lista.append(numero_int)
    elif numero_int < 0:
        print(lista)
        print(f'A média da lista é igual à {sum(lista)/len(lista):.2f}')
        break
