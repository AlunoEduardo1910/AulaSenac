ingresso = 49.02 #ingresso shopping continente
idade = int(input('Qual sua idade? '))
estudante = input("És estudante? (Sim ou Não)")

idade_12 = ingresso - (ingresso / 100 * 50)
estudante_desc = ingresso - (ingresso / 100 * 10)
idoso = ingresso - (ingresso / 100 * 30)

if idade < 12:
    print(f'O valor do ingresso é de {idade_12}')
elif idade >= 60:
    print(f'O valor do ingresso é de {idoso}')
elif estudante == 'Sim':
    print(f'O valor do ingresso é de {estudante_desc}')
else:
    print(f'O valor do ingresso é de {ingresso}')


