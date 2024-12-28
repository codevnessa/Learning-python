# Explicação do conteúdo: O desempacotamento permite extrair valores de uma tupla e atribuí-los a variáveis.
# Também é possível usar * para capturar o restante dos valores em uma lista.

# Exemplo de desempacotamento:
nomes = ("Maria", "Helena", "João")
nome1, nome2, nome3 = nomes  # Desempacota a tupla em três variáveis
print("Nomes:", nome1, nome2, nome3)

# Exemplo de desempacotamento com *:
numeros = (1, 2, 3, 4, 5)
primeiro, *resto = numeros  # Captura o primeiro valor e o restante em uma lista
print("Primeiro número:", primeiro)
print("Resto dos números:", resto)

# Explicação do código:
# 1. O desempacotamento atribui os valores da tupla a variáveis individuais.
# 2. O uso de *resto captura os valores restantes em uma lista.
# OBS: O desempacotamento é útil para trabalhar com múltiplos valores de forma organizada.