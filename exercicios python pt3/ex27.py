def encontrar_primeiro_ultimo_digito(numero):
    # confere se o número é negativo e o torna positivo
    if numero < 0:
        numero = -numero
    
    ultimo_digito = numero % 10
    primeiro_digito = numero
    
    # Encontrar o primeiro dígito
    while primeiro_digito >= 10:
        primeiro_digito = primeiro_digito // 10
    
    return primeiro_digito, ultimo_digito

def main():
    try:
        numero = int(input("Digite um número inteiro: "))
        primeiro_digito, ultimo_digito = encontrar_primeiro_ultimo_digito(numero)
        print(f"Primeiro dígito: {primeiro_digito}")
        print(f"Último dígito: {ultimo_digito}")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

if __name__ == "__main__":
    main()
