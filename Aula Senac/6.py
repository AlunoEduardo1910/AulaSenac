try:
    celsius = float(input("Digite a temperatura em Celsius:"))
    farenheit = (celsius * 9) / 5 + 32

    print(f"O valor em farenheit é {farenheit}.")

except:
    print("Por gentileza, colocar um número válido")
