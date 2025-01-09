# Diferença entre is e ==:
# is: Compara as identidades dos objetos (se são o mesmo objeto na memória).
# ==: Compara os valores dos objetos (se têm o mesmo conteúdo).

# Exemplo:
a = [1, 2, 3]
b = a  # b aponta para o mesmo objeto que a
c = [1, 2, 3]  # c é uma nova lista com os mesmos valores de a

# Comparando valores (==)
print(a == b)  # True (a e b têm o mesmo conteúdo)
print(a == c)  # True (a e c têm o mesmo conteúdo)
print("_______________")
# Comparando identidades (is)
print(a is b)  # True (a e b são o mesmo objeto na memória)
print(a is c)  # False (a e c são objetos diferentes na memória, mesmo tendo o mesmo conteúdo)
print("_______________")
# Explicação:
# O operador == verifica se os valores dos objetos são iguais, ou seja, se o conteúdo é o mesmo.
# O operador is verifica se os objetos são exatamente o mesmo na memória, ou seja, se apontam para o mesmo local.

# Outro exemplo:
x = 10
y = 10
z = 11

print(x == y)  # True (os valores são iguais)
print(x is y)  # True (para pequenos inteiros, Python reutiliza o mesmo objeto na memória)
print("_______________")
print(x == z)  # False (os valores são diferentes)
print(x is z)  # False (objetos diferentes na memória)

# Explicação adicional:
# Para tipos imutáveis como inteiros pequenos e strings, Python pode reutilizar o mesmo objeto na memória para otimização.
# Por isso, x is y pode retornar True para inteiros pequenos, mas isso não é garantido para todos os casos.
# Para objetos mutáveis, como listas, o operador is só retornará True se os objetos forem exatamente o mesmo.