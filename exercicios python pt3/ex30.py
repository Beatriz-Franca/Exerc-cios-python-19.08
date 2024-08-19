def verificar_palindromo(numero):
    # Converte o número para uma string para facilitar a manipulação
    numero_str = str(numero)
    
    inicio = 0
    fim = len(numero_str) - 1
    
    # Verifica os dígitos do início e do fim em direção ao centro
    while inicio < fim:
        if numero_str[inicio] != numero_str[fim]:
            return False  # Não é um palíndromo (palavra que pode ser lida normalmente ou de trás pra frente)
        inicio += 1
        fim -= 1
    
    return True  # É um palíndromo

def main():
    try:
        numero = int(input("Digite um número inteiro: "))
        if verificar_palindromo(numero):
            print(f"O número {numero} é um palíndromo.")
        else:
            print(f"O número {numero} não é um palíndromo.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

if __name__ == "__main__":
    main()

