# Tenta converter a entrada do usuário em um número inteiro
try:
    n = int(input("Digite um número: "))
except ValueError:
    # Se a conversão falhar (por exemplo, se o usuário digitar algo que não seja um número), exibe uma mensagem de erro
    print("Entrada inválida. Por favor, digite um número inteiro.")
    exit()  # Encerra o programa

# Loop para exibir a tabuada do número digitado
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")