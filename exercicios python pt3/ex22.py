#pede a entrada do usuário
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
#ler os valores de A e B e encontra o menor entre eles
def mdc(a, b):
    #calcula o mdc
    menor = min(a, b) 
    mdc = 1 
    for i in range(1, menor + 1):
        if a % i == 0 and b % i == 0:
            mdc = i 
    
    return mdc
resultado_mdc = mdc(numero1, numero2)
print(f"O Máximo Divisor Comum de {numero1} e {numero2} é {resultado_mdc}")