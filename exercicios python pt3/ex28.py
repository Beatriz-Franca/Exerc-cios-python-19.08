def inverter_digitos(numero):
    # Converte o número para uma string
    numero_str = str(numero)
    
    # Inverte a string
    numero_invertido_str = numero_str[::-1]
    
    # Converte a string invertida de volta para um inteiro
    numero_invertido = int(numero_invertido_str)
    
    return numero_invertido

def main():
    try:
        numero = int(input("Digite um número inteiro: "))
        numero_invertido = inverter_digitos(numero)
        print(f"Resultado da inversão dos dígitos: {numero_invertido}")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

if __name__ == "__main__":
    main()
