try:
    numero_1 = float(input("Dê um número: "))
    operacao = input("Qual a operação desejada (adição, subtração, multiplicação ou divisão)? ")
    numero_2 = float(input("Dê outro número: "))

    if numero_2 == 0 and operacao == "divisão":
        print("Impossível dividir por 0")
    elif operacao == "adição":
        print(numero_1 + numero_2)
    elif operacao == "subtração":
        print(numero_1 - numero_2)
    elif operacao == "multiplicação":
        print(numero_1 * numero_2)
    elif operacao == "divisão":
        print(numero_1 / numero_2)
    else:
        print("Operação inválida")
except:
    print("Digite um número válido")
