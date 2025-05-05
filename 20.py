while True:
    try:
        numero = int(input("Tente advinhar o número de 1 a 10: "))
        if numero >= 9:
            print("Muito alto")
        elif numero == 8:
            print("Um pouco mais para baixo")
        elif numero > 4 and numero < 7:
            print("Um pouco mais pra cima")
        elif numero <= 4:
            print("Muito baixo")
        elif numero == 7:
            print("Excelente, você acertou")
            break
    except:
        print("Número inválido")
