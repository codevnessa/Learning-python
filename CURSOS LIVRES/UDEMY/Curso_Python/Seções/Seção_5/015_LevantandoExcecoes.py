class MeuError(Exception): 
    ...
    
class OutroError(Exception): 
    ...    
    
def levantar():
    exception_ = MeuError('a','b', 'c')
    raise exception_
try:
    #1/0
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    exception_ = OutroError('Vou lançar de novo')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('Mais uma nota')
    
    raise exception_ from error