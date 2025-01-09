# Operador Lógico AND
# O operador AND retorna True apenas se todas as condições envolvidas forem verdadeiras. Caso contrário, retorna False.

# Exemplo prático:
idade = 25
tem_carteira = True

# Verifica se a pessoa tem mais de 18 anos E tem carteira de motorista
if idade > 18 and tem_carteira:
    print("Pode dirigir!")
else:
    print("Não pode dirigir.")

# Explicação:
# idade > 18 → True (25 é maior que 18).
# tem_carteira → True (a variável é True).
# Como ambas as condições são True, a expressão inteira é avaliada como True, e o programa imprime "Pode dirigir!".