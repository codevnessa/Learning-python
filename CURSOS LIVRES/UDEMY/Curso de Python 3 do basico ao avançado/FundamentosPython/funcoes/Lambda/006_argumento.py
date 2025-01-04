# Como passar uma função lambda como argumento para outra função:

# Função que aplica uma operação a um número
def aplicar_operacao(x, operacao):
    return operacao(x)

# Usando a função lambda como argumento
resultado = aplicar_operacao(5, lambda x: x * 3)
print(resultado)  # Resultado: 15


# 1. `aplicar_operacao` é uma função que recebe um número (x) e uma operação (outra função).
# 2. `lambda x: x * 3` é uma função lambda que multiplica x por 3.
# 3. `aplicar_operacao(5, lambda x: x * 3)` chama a função `aplicar_operacao`, passando 5 e a função lambda.
# 4. A função lambda é executada dentro de `aplicar_operacao`, resultando em 15.