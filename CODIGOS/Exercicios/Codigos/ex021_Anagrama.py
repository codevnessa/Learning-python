def anagrama(palavra, palavra_):
    palavra = palavra.replace(" ", "").upper()
    palavra_ = palavra_.replace(" ", "").upper()
    
    if len(palavra) != len(palavra_):
        return False
    
    return sorted(palavra) == sorted(palavra_)

# Exemplos de uso
print(anagrama("listen", "silent"))  # True
print(anagrama("amor", "roma"))      # True
print(anagrama("casa", "saco"))      # False
print(anagrama("anagrama", "manga")) # False