# Projeto 2 - Desenvolvimento de Game em Linguagem Python - Versão 2

# Import
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpatela():

    # Windows
    if name == 'nt':
        _ = system('cls')
    
    # Mac ou Linux
    else:
        _ = system('clear')


estagios = [ 
# estágio 6 (final)
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

# Classe
class Hangman:

	# Método Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_descobertas = []

    # Método para adivinhar a letra
    def guess(self, letra):

        if letra in self.palavra and letra not in self.letras_descobertas:
            self.letras_descobertas.append(letra)

        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        
        else:
            return False
        
        return True
        
    # Método para verificar se o jogo terminou    
    def hangman_over(self):
        return self.hangman_won() or (len(self.letras_erradas) == 6)

    # Método para verificar se o jogador venceu  
    def hangman_won(self):

        if '_' not in self.hide_palavra():
            return True
        return False  
      
    # Método para não mostrar a letra no board  
    def hide_palavra(self):

        rtn = ''

        for letra in self.palavra:
            if letra not in self.letras_descobertas:
                rtn += '_'
            else:
                rtn += letra
        return rtn
	
    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):

        print(estagios[len(self.letras_erradas)])

        print('\nPalavra: ' + self.hide_palavra())  
      
        print('\nLetras erradas: ',)

        for letra in self.letras_erradas:
            print(letra,)

        print() 

        print('Letras corretas: ',)

        for letra in self.letras_descobertas:
            print(letra,)

        print()

# Método para ler uma palavra de forma aleatória do banco de palavras
def rand_palavra():

    with open('Cap07/ListadeObjetos.txt','r') as arquivo:
        palavras = arquivo.read().split(",")
    

    palavras_s = [wordl.strip() for wordl in palavras]
    
    # Escolhe aleatoriamente uma palavra
    palavra = random.choice(palavras_s) 

    return palavra	

# Método Main - Execução do Programa
def main():

    limpatela()

	# Cria o objeto e seleciona uma palavra randomicamente
    game = Hangman(rand_palavra().lower())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter    
    while not game.hangman_over():
        
        #  Status do game
        game.print_game_status()

        # Recebe input do terminal
        user_input = input('\nDigite uma letra: ')

        # Verifica se a letra digitada faz parte da palavra
        game.guess(user_input.lower())

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!')
    
    else:
        print('\nGame Over! Você perdeu.')
        print ('A palavra era ' + game.palavra)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa
if __name__ == "__main__":
    main()