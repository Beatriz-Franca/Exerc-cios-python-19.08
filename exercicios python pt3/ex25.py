def exibir_numeros_impares_while(x):
    print(f"Números ímpares de 1 a {x}:")
    i = 1
    while i <= x:
        if i % 2 != 0:
            print(i, end=' ')
        i += 1
    print()  # Para garantir uma nova linha depois da saída dos números

def main():
    try:
        x = int(input("Digite um número inteiro positivo x: "))
        if x < 1:
            print("Por favor, insira um número inteiro positivo maior ou igual a 1.")
        else:
            exibir_numeros_impares_while(x)
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

if __name__ == "__main__":
    main()
