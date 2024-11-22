Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Olá mundo")
Olá mundo
>>> print(7+4
... )
11
>>> 7+4
11
>>> '7'+'4'
'74'
>>> print('ola' +5)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print('ola' +5)
TypeError: can only concatenate str (not "int") to str
>>> print('ola' , 5)
ola 5
>>> nome = 'Vanessa'
>>> idade=21
>>> 
>>> idade = 21
>>> peso = 90
>>> print(nome, idade, peso)
Vanessa 21 90
>>> print(nome+ idade + peso)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(nome+ idade + peso)
TypeError: can only concatenate str (not "int") to str
>>> nome=input('Qual é o seu nome
...            
SyntaxError: unterminated string literal (detected at line 1)
>>> nome= input('Qual é o seu nome')
...            
Qual é o seu nome
>>> idade = input ('Qual a sua idade?
...                
SyntaxError: unterminated string literal (detected at line 1)
>>> idade = input ('Qual a sua idade?')
...                
Qual a sua idade? 21
Qual a sua idade? 21
               
SyntaxError: invalid syntax
