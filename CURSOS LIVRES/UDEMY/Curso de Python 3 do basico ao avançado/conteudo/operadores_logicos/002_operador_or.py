# Operador Lógico OR
# O operador OR retorna True se pelo menos uma das condições envolvidas for verdadeira. Caso contrário, retorna False.

# Exemplo prático:
idade = 15
tem_carteira = False

# Verifica se a pessoa tem mais de 18 anos OU tem carteira de motorista
if idade > 18 or tem_carteira:
    print("Pode dirigir!")
else:
    print("Não pode dirigir.")

# Explicação:
# idade > 18 → False (15 não é maior que 18).
# tem_carteira → False (a variável é False).
# Como ambas as condições são False, a expressão inteira é avaliada como False, e o programa imprime "Não pode dirigir.".