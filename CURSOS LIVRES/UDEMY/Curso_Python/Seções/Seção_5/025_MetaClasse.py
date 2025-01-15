"""
Em Python, tudo é um objeto, incluindo as classes, que são, por sua vez, instâncias de metaclasses. 
A metaclasse padrão em Python é type, e é ela que define como as classes são criadas e comportam-se. 
Quando você cria uma classe, o método especial __new__ da metaclasse é chamado primeiro para criar a nova classe, seguido pelo método __call__, que cuida da criação de instâncias, chamando os métodos __new__ e __init__ da classe. 
Esses métodos têm responsabilidades distintas: __new__ cria o objeto, enquanto __init__ o inicializa. 
A função type pode ser usada para criar classes dinamicamente, seguindo a sintaxe type('Name', (Bases,), __dict__). 
Embora metaclasses permitam personalizar profundamente o comportamento das classes, são uma ferramenta avançada que a maioria dos desenvolvedores não precisa usar, como destacou Tim Peters, um dos principais desenvolvedores do Python: 
"Se você precisa saber sobre metaclasses, provavelmente não precisa delas."
"""

#class Foo:
#    ...
    
Foo = type('Foo', (object,), {})
f = Foo()
# print(isinstance(f, Foo))
print(type(f))
print(type(Foo))