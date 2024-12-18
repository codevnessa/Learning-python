n = int(input("Digite um número: "))
def num_primo(n):
	if n <= 1:
		return False
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
	return True

def nums_primos_ate(n):
	nums_primos = []
	for i in range (2, n + 1):
		if num_primo(i):
			nums_primos.append(i)
	return nums_primos

primos = nums_primos_ate(n)
print(f"Numeros primos até {n}:\n{', '.join(map(str, primos))}.")