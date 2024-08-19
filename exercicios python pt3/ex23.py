def verificar_numero_perfeito(numero):
    if numero <= 0:
        return False
    
    soma_divisores = 0
    # Encontra todos os divisores próprios do número
    for i in range(1, numero):
        if numero % i == 0:
            soma_divisores += i
    
    # Verifica se a soma dos divisores é igual ao número
    return soma_divisores == numero

def main():
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        if numero <= 0:
            print("Por favor, insira um número inteiro positivo.")
        else:
            if verificar_numero_perfeito(numero):
                print(f"{numero} é um número perfeito.")
            else:
                print(f"{numero} não é um número perfeito.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

if __name__ == "__main__":
    main()
