v = int(input('Sua velocidade em km/h:'''))
print('MULTADO EM R${} REAIS'.format((v - 80) * 7)if v>80 else 'UFA, NAO FOI MULTADO !')
