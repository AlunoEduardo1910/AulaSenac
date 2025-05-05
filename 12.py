lista = []

for i in range(3):
    numeros = input(f'Digite o {i+1}º numero: ')
    lista.append(numeros)

lista.sort()

print(lista)
