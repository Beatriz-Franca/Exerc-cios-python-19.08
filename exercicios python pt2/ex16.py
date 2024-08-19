N_str = input("Digite o valor de N: ")

try:
    N = int(N_str)
    
    if N < 1:
        print("Insira um número inteiro positivo.")
    else:
        contador = 1
        soma = 0
        while contador <= N:
            soma += contador
            contador += 1
        print(f"A soma dos números de 1 até {N} é: {soma}")

except ValueError:
    print("Por favor, insira um número inteiro válido.")
