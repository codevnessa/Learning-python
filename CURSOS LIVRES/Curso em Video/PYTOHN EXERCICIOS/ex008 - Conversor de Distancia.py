med = float(input('Qual distancia em metros:'))
cm = med * 100
mm = med * 1000
km = med / 1000
hm = med / 100
dam = med / 10
dm = med * 10
print('Centimentros: {:.0f}cm\nMilimetros: {:.0f}mm\nQuilometros: {}km\nHectômetro: {}hm\nDecâmetros: {}dam\nDecímetros: {}dm'.format(cm, mm,km, hm,dam, dm))