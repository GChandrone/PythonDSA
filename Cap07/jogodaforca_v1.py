# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 1

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
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / \\
        -
     """,
     # estágio 5
     """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / 
        -
     """,
     # estágio 4
     """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |      
        -
     """,
     # estágio 3
     """
        --------
        |      |
        |      O
        |     \\|
        |      |
        |     
        -
     """,
     # estágio 2
     """
        --------
        |      |
        |      O
        |      |
        |      |
        |     
        -
     """,
     # estágio 1
     """
        --------
        |      |
        |      O
        |    
        |      
        |     
        -
     """,
     # estágio 0
     """
        --------
        |      |
        |      
        |    
        |      
        |     
        -
     """
    ]
    return estagios[chances]

# Função Principal
def game():

    limpatela()
    
    print("\nBem-Vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    # Lista de palavras para o jogo
    palavras = ['Banana', 'Uva', 'Morango', 'Laranja', 'Abacate', 'Manga']
   
    # Escolhe aleatoriamente uma palavra
    palavra = random.choice(palavras) 
    
    # List comprehension
    letras_descobertas = ['_' for letra in palavra]

    # Número de chances
    chances = 6

    # Lista de palavras erradas
    letras_erradas = []

    frase = " "

    while chances > 0:

        limpatela()

        # Print
        print(desenho_boneco(chances))
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))
        print("\n",frase)
        # Tentativa
        tentativa = input("\nDigite uma letra: ").lower()

        # Condicional
        if tentativa in palavra.lower():
            index = 0

            for letra in palavra:
                if tentativa == letra.lower():
                    letras_descobertas[index] = letra
                    if tentativa in letras_descobertas and tentativa in letras_erradas:
                        frase = "Está letra já foi digitada"
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        # Condicional
        if "_" not in letras_descobertas:
            limpatela()
            print(desenho_boneco(chances))
            print(" ".join(letras_descobertas))
            print("\nParabéns você venceu!")
            print("\nChances restantes:", chances)
            print("Letras erradas:", " ".join(letras_erradas))
            break
            
    # Condicional        
    if "_" in letras_descobertas:
        limpatela()
        print(desenho_boneco(chances))
        print("\nVocê Perdeu, a palavra era", palavra)

# Bloco Main
if __name__ == "__main__":
    game()
    print("\nDeus me ajuda a aprender e entender tudo. Amém!!\n") 
