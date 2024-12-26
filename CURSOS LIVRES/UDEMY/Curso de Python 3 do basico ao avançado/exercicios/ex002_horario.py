# Solicita ao usuário que digite a hora atual e converte o valor para float
hora = float(input("Qual a hora atual? "))

# Verifica o intervalo de horas e exibe uma mensagem correspondente
if 0 <= hora <= 5:
    print("LUAR DA MADRUGADA! 🌙")  # Mensagem para a madrugada
elif 6 <= hora < 12:
    print("SOL BRILHANDO, HORA DE AGIR! ☀️")  # Mensagem para a manhã
elif hora == 12:
    print("HORA DO COMBUSTÍVEL! 🍴")  # Mensagem para o meio-dia
elif 12 < hora <= 18:
    print("TARDE DE CONQUISTAS! 🚀")  # Mensagem para a tarde
else:
    print("ESTRELAS NO CÉU, SONHOS NO CORAÇÃO! 🌟")  # Mensagem para a noite