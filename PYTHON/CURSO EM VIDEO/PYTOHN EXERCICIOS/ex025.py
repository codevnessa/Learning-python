nome = str(input('Digite o seu nome:').strip())
tem_silva = 'SILVA' in nome.upper()
if not tem_silva:
    print('SEU NOME INFELIZMENTE NAO TEM SILVA, VOCE É UMA PESSOA RARA')
else:
    print('SEU NOME TEM SILVA, PARABÉNS É UM NOME COMUM!!')