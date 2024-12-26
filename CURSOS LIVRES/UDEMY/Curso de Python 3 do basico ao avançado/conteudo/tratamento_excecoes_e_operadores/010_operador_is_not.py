# Operador is not
# O operador is not é o oposto do operador is. Ele verifica se dois objetos não são o mesmo objeto na memória.

# Sintaxe:
# objeto1 is not objeto2

# Exemplo prático:
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is not b)  # False 
print(a is not c)  # True

# Explicação:
# a e b são o mesmo objeto, então a is not b retorna False.
# a e c são objetos diferentes, então a is not c retorna True.