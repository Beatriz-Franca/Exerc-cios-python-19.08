# Solicita ao usuário a quantidade de fotocópias realizadas
quantidade = int(input("Digite a quantidade de fotocópias realizadas: "))

# Calcula o custo com base nas regras fornecidas
if quantidade <= 10:
    custo = quantidade * 0.25
elif quantidade <= 30:
    custo = 10 * 0.25 + (quantidade - 10) * 0.20
else:
    custo = 10 * 0.25 + 20 * 0.20 + (quantidade - 30) * 0.10

# Exibe a fatura correspondente
print(f"O custo total é R$ {custo:.2f}")
