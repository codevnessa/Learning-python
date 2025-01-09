# Introdução às Generator functions em Python

# Definindo uma função geradora
def generator(n=0, maximum=10):
    """
    Função geradora que produz valores de n até maximum - 1.
    - n: Valor inicial (padrão é 0).
    - maximum: Valor máximo (não inclusivo). Quando n >= maximum, o gerador para.
    """
    while True:  # Loop infinito
        yield n  # Produz o valor atual de n e pausa a execução da função
        n += 1   # Incrementa n para o próximo valor

        # Condição de parada: se n atingir ou ultrapassar maximum, encerra o gerador
        if n >= maximum:
            return  # Encerra a função geradora

# Criando um gerador que produz valores de 0 a 999999
gen = generator(maximum=100)  # Gerador configurado para produzir até 1.000.000 de valores

# Iterando sobre o gerador e imprimindo os valores
for n in gen:
    print(n)  # Imprime cada valor produzido pelo gerador

# Explicação dos conceitos:
# - Função geradora: Uma função que usa a palavra-chave yield para produzir valores sob demanda.
#   Ela retorna um objeto gerador, que pode ser iterado.

# - yield: Produz um valor e pausa a execução da função. Quando a função é chamada novamente,
#   ela continua de onde parou.

# - Lazy evaluation: Os valores são gerados apenas quando necessários, economizando memória.
#   Isso é útil para sequências grandes ou infinitas.

# - return em geradores: Encerra a função geradora, levantando uma exceção StopIteration,
#   que é tratada automaticamente pelo loop for.


# - A função generator produz valores de n até maximum - 1.
# - O gerador gen é criado para produzir valores de 0 a 999999.
# - O loop for itera sobre o gerador, imprimindo cada valor.
# - Como o gerador usa lazy evaluation, ele não armazena todos os 1.000.000 de valores na memória de uma vez.