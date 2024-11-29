# Define a função para_base que converte um número para uma base específica
def para_base(n, base):
    # Se o número for 0, retorna "0"
    if n == 0:
        return "0"
    
    # Define uma string com os dígitos possíveis (de 0 a F)
    digitos = "0123456789ABCDEF"
    
    # Inicializa a string resultado
    resultado = ""
    
    # Loop enquanto o número for maior que 0
    while n > 0:
        # Adiciona o dígito correspondente ao resto da divisão de n pela base
        resultado = digitos[n % base] + resultado
        # Atualiza n para a divisão inteira de n pela base
        n //= base
    
    # Retorna o resultado da conversão
    return resultado

# Solicita ao usuário que digite um número
n = int(input("Digite um número: "))

# Solicita ao usuário que digite a base para a conversão (entre 2 e 16)
base = int(input("Digite a base (2-16): "))

# Converte o número para a base especificada e exibe o resultado
print(f"O número {n} na base {base} é {para_base(n, base)}")