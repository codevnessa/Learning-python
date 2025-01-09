# Classe Camera: mantém o estado de filmagem e permite operações relacionadas
class Camera:
    
    # Método construtor: inicializa a câmera com um nome e estado de filmagem
    def __init__(self, nome, filmando=False):
        self.nome = nome  
        self.filmando = filmando  # Atributo da instância: estado de filmagem (True/False)

    # Método para iniciar a filmagem
    def filmar(self):
        if self.filmando: 
            print(f'{self.nome} JÁ está filmando...')  
            return

        print(f'{self.nome} está filmando...')  
        self.filmando = True  

    # Método para parar a filmagem
    def parar_filmar(self):
        if not self.filmando:  
            print(f'{self.nome} NÃO está filmando...') 
            return

        print(f'{self.nome} está parando de filmar...') 
        self.filmando = False  
        
    # Método para fotografar
    def fotografar(self):
        if self.filmando: 
            print(f'{self.nome} não pode fotografar filmando')
            return

        print(f'{self.nome} está fotografando...')  # Tira uma foto


# Cria duas instâncias da classe Camera com nomes diferentes
c1 = Camera('Canon') 
c2 = Camera('Sony')  

# Testando operações com a câmera Canon (c1)
c1.filmar()       
c1.filmar()      
c1.fotografar()   
c1.parar_filmar()
c1.fotografar()  

print()  

# Testando operações com a câmera Sony (c2)
c2.parar_filmar()
c2.filmar()      
c2.filmar()       
c2.fotografar()  
c2.parar_filmar() 
c2.fotografar()  