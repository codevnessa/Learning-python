# Define a função eh_primo que verifica se um número é primo
def e_primo(n):
    # Se o número for menor ou igual a 1, não é primo
    if n <= 1:
        return False
    # Loop para verificar divisibilidade até a raiz quadrada de n
    for i in range(2, int(n**0.5) + 1):
        # Se n for divisível por algum número, não é primo
        if n % i == 0:
            return False
    # Se não encontrou divisores, o número é primo
    return True

# Solicita ao usuário que digite um número
n = int(input("Digite um número: "))

# Verifica se o número é primo usando a função eh_primo
if e_primo(n):
    print(f"{n} é primo.")
else:
    print(f"{n} não é primo.")