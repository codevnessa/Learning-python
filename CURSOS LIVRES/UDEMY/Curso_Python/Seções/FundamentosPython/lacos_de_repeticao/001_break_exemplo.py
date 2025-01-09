# Explicação do assunto: O break é usado para interromper um loop imediatamente.
# Quando o Python encontra um break, ele sai do loop, independentemente da condição do loop.
# Isso é útil quando você quer parar a execução do loop com base em uma condição específica.

# Exemplo de uso do break:
contador = 0  # Inicializa o contador com 0

while contador < 10:  # Enquanto o contador for menor que 10
    print(contador)  # Imprime o valor atual do contador
    if contador == 4:  # Se o contador for igual a 4
        break  # Interrompe o loop imediatamente
    contador += 1  # Incrementa o contador em 1

# Explicação do código:
# 1. O contador começa em 0.
# 2. O loop while continua enquanto o contador for menor que 10.
# 3. A cada iteração, o valor do contador é impresso.
# 4. Quando o contador chega a 4, o break é executado, interrompendo o loop.
# 5. O programa continua executando o código após o loop.
# OBS: O break é útil para sair de loops quando uma condição específica é atendida.