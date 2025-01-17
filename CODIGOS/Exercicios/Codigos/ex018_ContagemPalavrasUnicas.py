import re
from collections import defaultdict

def contador(texto):
    texto = texto.upper()
    texto = re.sub(r'[^\w\s]', '', texto)
    palavras = texto.split()
    palavras_ = set(palavras)
    
    frequencia = defaultdict(int)
    for palavra in palavras:
        frequencia[palavra] += 1
    
    repeticao = {f'{palavra}: {count}' for palavra, count in frequencia.items() if count > 1}
        
    return len(palavras_), repeticao

texto = "Quem tem boca vai a Roma, e quem tem pressa não espera. Tem que ter paciência, não adianta correr!"
quantidade, repetidas = contador(texto)
print(f'Numero de palavras unicas: {quantidade}')
print(f'Palavras repetidas: \n{'\n'.join(repetidas)}')