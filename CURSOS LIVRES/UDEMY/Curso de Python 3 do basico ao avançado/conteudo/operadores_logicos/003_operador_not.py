# Operador Lógico NOT
# O operador NOT inverte o valor booleano de uma expressão. Ele retorna True se a expressão for False, e retorna False se a expressão for True.

# Exemplo prático:
tem_carteira = False

# Verifica se a pessoa NÃO tem carteira de motorista
if not tem_carteira:
    print("Não tem carteira de motorista.")
else:
    print("Tem carteira de motorista.")

# Explicação:
# tem_carteira → False.
# not tem_carteira → True (inverte o valor).
# Como a expressão é True, o programa imprime "Não tem carteira de motorista.".