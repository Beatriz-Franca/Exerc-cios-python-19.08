
def determinar_categoria(idade):
    if 6 <= idade <= 7:
        return "pequeno de 6 a 7 anos"
    elif 8 <= idade <= 9:
        return "aluno1 de 8 a 9 anos"
    elif 10 <= idade <= 11:
        return "aluno2 de 10 a 11 anos"
    elif idade >= 12:
        return "aluno3 >= 12 anos"
    else:
        return "Idade fora das categorias definidas"


idade_str = input("Digite a idade da criança: ")

try:
    idade = int(idade_str)
    categoria = determinar_categoria(idade)
    print(f"A categoria da criança é: {categoria}")
except ValueError:
    print("Por favor, digite um número válido para a idade.")
