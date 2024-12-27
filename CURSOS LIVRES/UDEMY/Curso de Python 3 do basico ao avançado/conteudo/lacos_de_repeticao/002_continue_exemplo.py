# Explicação do assunto: O continue é usado para pular a iteração atual de um loop e voltar para o início.
# Quando o Python encontra um continue, ele ignora o restante do bloco de código e começa a próxima iteração.
# Isso é útil quando você quer ignorar uma iteração específica com base em uma condição.

# Exemplo de uso do continue:
contador = 0  # Inicializa o contador com 0

while contador < 10:  # Enquanto o contador for menor que 10
    contador += 1  # Incrementa o contador em 1
    if contador == 6:  # Se o contador for igual a 6
        continue  # Pula a iteração atual e volta para o início do loop
    print(contador)  # Imprime o valor atual do contador

# Explicação do código:
# 1. O contador começa em 0.
# 2. O loop while continua enquanto o contador for menor que 10.
# 3. A cada iteração, o contador é incrementado em 1.
# 4. Quando o contador chega a 6, o continue é executado, pulando o print e voltando para o início do loop.
# 5. O loop continua até que o contador seja 10.
# OBS: O continue é útil para ignorar iterações específicas sem interromper o loop completamente.