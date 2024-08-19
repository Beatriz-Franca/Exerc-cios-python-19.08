def calcular_soma_digitos(numero):
    # Converte o número para valor absoluto para tratar números negativos
    numero = abs(numero)
    
    soma = 0
    # Converte o número para string para iterar sobre cada dígito
    numero_str = str(numero)
    
    for digito in numero_str:
        soma += int(digito)  # Converte o caractere de volta para inteiro e soma
    
    return soma

def main():
    try:
        numero = int(input("Digite um número inteiro: "))
        soma_digitos = calcular_soma_digitos(numero)
        print(f"A soma dos dígitos do número {numero} é: {soma_digitos}")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

if __name__ == "__main__":
    main()
