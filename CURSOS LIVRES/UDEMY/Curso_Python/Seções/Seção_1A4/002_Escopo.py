""" 
O escopo em Python determina onde uma parte do código pode ser usada. 
Existem dois tipos principais de escopo: o global e o local. 
O escopo global é como uma área aberta onde tudo no código pode ser acessado. 
Já o escopo local é mais restrito, como um espaço fechado, onde apenas as variáveis ou funções criadas dentro dele podem ser usadas. 
Por exemplo, uma variável definida dentro de uma função só existe enquanto a função está sendo executada; fora dela, não pode ser acessada.
"""

# Escopo Global
variavel_global = "Eu estou em todo lugar!"

def minha_funcao():
    # Escopo Local
    variavel_local = "Eu só existo aqui dentro!"
    print(variavel_global)  # Posso acessar a variável global
    print(variavel_local)   # Posso acessar a variável local

minha_funcao()

# Isso vai dar erro, porque variavel_local só existe dentro da função
print(variavel_global)

