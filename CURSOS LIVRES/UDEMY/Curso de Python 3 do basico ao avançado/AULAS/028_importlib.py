import importlib
import modulo
print(modulo.variavel)
for i in range(10):
    importlib.reload(modulo)
    print(i)
print('Fim')