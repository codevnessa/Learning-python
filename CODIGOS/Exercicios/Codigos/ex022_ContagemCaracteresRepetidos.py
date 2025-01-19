import re

def contador(texto):
    # Remove tudo que não é letra (usando expressões regulares)
    texto = re.sub(r"[^A-Za-zÀ-ÖØ-öø-ÿ]", "", texto.upper())
    
    contagem = {}
    for letra in texto:
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1

    for letra, quantidade in contagem.items():
        print(f"{letra}: {quantidade}")

texto = "Quem tem boca vai a Roma, e quem tem pressa não espera. Tem que ter paciência, não adianta correr!"

contador(texto)