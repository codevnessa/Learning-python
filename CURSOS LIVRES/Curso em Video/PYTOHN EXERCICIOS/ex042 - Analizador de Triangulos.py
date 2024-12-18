seg1 = int(input("Primeiro segmento: "))
seg2 = int(input("Segundo segmento: "))
seg3 = int(input("Terceiro segmento: "))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
	print("Esses segmentos podem formar um triagulo")
	if seg1 == seg2 == seg3:
		print("Esses segmentos formaram um triangulo EQUILÁTERO!")
	elif seg1 != seg2 != seg3:
		print("Esses segmentos formaram um triangulo ESCALENO!")
	else:
		print("Esses segmentos formaram um triangulo ISÓSCELES!")
else:
	print("Esses segmentos nao podem formar um triagulo")



