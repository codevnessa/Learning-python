lista = ["banana", "maçã", "laranja", "uva", "melancia"]
tam = list(filter(lambda palavra: len(palavra) >= 4,lista))
print(tam)