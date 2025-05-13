mes = input("Qual mês gostarias de saber a quantidade de dias? ")
match mes:
    case "Janeiro":
        print(f'O mês de {mes} tem 31 dias')
    case "Fevereiro":
        print(f'O mês de {mes} tem 28 dias')
    case "Março":
        print(f'O mês de {mes} tem 31 dias')
    case "Abril":
        print(f'O mês de {mes} tem 30 dias')
    case "Maio":
        print(f'O mês de {mes} tem 31 dias')
    case "Junho":
        print(f'O mês de {mes} tem 30 dias')
    case "Julho":
        print(f'O mês de {mes} tem 31 dias')
    case "Agosto":
        print(f'O mês de {mes} tem 31 dias')
    case "Setembro":
        print(f'O mês de {mes} tem 30 dias')
    case "Outubro":
        print(f'O mês de {mes} tem 31 dias')
    case "Novembro":
        print(f'O mês de {mes} tem 30 dias')
    case "Dezembro":
        print(f'O mês de {mes} tem 31 dias')
    case _:
        print("Mês inválido")
