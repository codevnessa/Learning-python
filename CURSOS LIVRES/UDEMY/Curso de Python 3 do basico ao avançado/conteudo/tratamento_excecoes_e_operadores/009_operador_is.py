# Operador is
# O operador is é usado para verificar se dois objetos são exatamente o mesmo objeto na memória. Ele compara as identidades dos objetos, não seus valores.

# Sintaxe:
# objeto1 is objeto2

# Exemplo prático:
a = [1, 2, 3]
b = a  # b aponta para o mesmo objeto que a
c = [1, 2, 3]

print(a is b)  # True (a e b são o mesmo objeto)
print(a is c)  # False (a e c têm o mesmo valor, mas são objetos diferentes)

# Explicação:
# a e b apontam para o mesmo objeto na memória, então a is b retorna True.
# a e c têm o mesmo valor, mas são objetos diferentes na memória, então a is c retorna False.