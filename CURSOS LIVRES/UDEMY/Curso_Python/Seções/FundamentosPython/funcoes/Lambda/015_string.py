# Funções lambda para manipular strings.

# Função lambda que inverte uma string
inverter = lambda s: s[::-1]

# Usando a função lambda
resultado = inverter("Python")
print(resultado)  # Resultado: nohtyP

# 1. `lambda s:` cria uma função lambda que recebe uma string (s).
# 2. `s[::-1]` inverte a string.
# 3. `inverter("Python")` chama a função lambda, passando "Python" como s.
# 4. O resultado ("nohtyP") é exibido.