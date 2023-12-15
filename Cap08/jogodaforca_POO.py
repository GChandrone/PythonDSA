# Projeto 2 - Desenvolvimento de Game em Linguagem Python - Versão 2

# Import
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpatela():

    if name == 'nt':
        system('cls')
    else:
        system('clear')

# Função que desenha a forca na tela
def desenho_boneco(chances):

    # Lista de estágios da forca
    estagios = [ # estágio 6 (final)
     """
        +------+
        |      |
        |      O
        |     \\|/
        |      |
        |     / \\
        -
     """,
     # estágio 5
     """
        +------+
        |      |
        |      O
        |     \\|/
        |      |
        |     / 
        -
     """,
     # estágio 4
     """
        +------+
        |      |
        |      O
        |     \\|/
        |      |
        |      
        -
     """,
     # estágio 3
     """
        +------+
        |      |
        |      O
        |     \\|
        |      |
        |     
        -
     """,
     # estágio 2
     """
        +------+
        |      |
        |      O
        |      |
        |      |
        |     
        -
     """,
     # estágio 1
     """
        +------+
        |      |
        |      O
        |    
        |      
        |     
        -
     """,
     # estágio 0
     """
        +------+
        |      |
        |      
        |    
        |      
        |     
        -
     """
    ]
    return estagios[chances]

# Classe
class Hangman:

	# Método Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_digitas = []

    def guess(self, letra):

        if letra in self.palavra and letra not in self.letras_digitas:
            self.letras_digitas.append(letra)

        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        
        else:
            return False
        
        return True
        
    def hangman_over(self):
        return self.hangman_won() or len(self.letras_erradas == 6)

        # List comprehension
        self.letras_descobertas = ['_' for letra in self.palavra]

        # Número de chances
        self.chances = 6

        # Lista de palavras erradas
        self.letras_erradas = []

        # Lista de palavras digitadas
        self.letras_digitas = []

	# Método para adivinhar a letra
    def tentativa(self):
             
             tentativa = input("\nDigite uma letra: ").lower()
             
             while tentativa in self.letras_digitas or len(tentativa) > 1 or tentativa.isalpha() == False:
                
                limpatela()

                # Print
                print(desenho_boneco(self.chances))
                print(" ".join(self.letras_descobertas))
                print("\nChances restantes:", self.chances)
                print("Letras erradas:", " ".join(self.letras_erradas))
                
                if tentativa in self.letras_digitas:
                    print("\nEsta letra já foi digitada. Tente Novamente!")
                elif len(tentativa) > 1:
                    print("\nDigite apenas UMA letra. Tente Novamente!")
                elif tentativa.isalpha() == False:
                    print("\nDigite apenas LETRAS. Tente Novamente!")
                tentativa = input("\nDigite uma letra: ").lower()
                    
                if tentativa not in self.letras_digitas:
                    self.letras_digitas.append(tentativa)
                    
                # Condicional
                if tentativa in self.palavra.lower():
                    index = 0

                    for letra in self.palavra:
                        if tentativa == letra.lower():
                            self.letras_descobertas[index] = letra
                        index += 1
                else:
                    self.chances -= 1
                    self.letras_erradas.append(tentativa)
        
	# Método para verificar se o jogo terminou
    def terminou(self):
        
            if "_" in self.letras_descobertas:
                limpatela()
                print(desenho_boneco(self.chances))
                print("\nVocê Perdeu, a palavra era", self.palavra, "\n")	

	# Método para verificar se o jogador venceu
    def venceu(self):
        # Condicional
        if "_" not in self.letras_descobertas:
            limpatela()
            print(desenho_boneco(self.chances))
            print(" ".join(self.letras_descobertas))
            print("\nParabéns você venceu!")
            print("\nChances restantes:", self.chances)
            print("Letras erradas:", " ".join(self.letras_erradas), "\n")
	
    # Método para não mostrar a letra no board
		
	# Método para checar o status do game e imprimir o board na tela

def rand_palavra():

    with open('Cap07/ListadeObjetos.txt','r') as arquivo:
            palavras = arquivo.read().split(",")
    
        palavras_s = [wordl.strip() for wordl in palavras]
        
        # Escolhe aleatoriamente uma palavra
        palavra = random.choice(palavras_s) 

        return palavra

def main():
    
    limpatela()

    game = 

