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

    # Pegando a Lista de palavras por um arquivo txt
    with open('Cap07/ListadeObjetos.txt','r') as arquivo:
        palavras = arquivo.read().split(",")
    
    palavras_s = [wordl.strip() for wordl in palavras]
    
    # Escolhe aleatoriamente uma palavra
    palavra = random.choice(palavras_s) 
    
    # List comprehension
    letras_descobertas = ['_' for letra in palavra]

    # Número de chances
    chances = 6

    # Lista de palavras erradas
    letras_erradas = []

    # Lista de palavras digitadas
    letras_digitas = []

    while chances > 0:

        limpatela()

        # Print
        print(desenho_boneco(chances))
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))
                
        # Tentativa
        tentativa = input("\nDigite uma letra: ").lower()


        while tentativa in letras_digitas or len(tentativa) > 1 or tentativa.isalpha() == False:
            limpatela()

            # Print
            print(desenho_boneco(chances))
            print(" ".join(letras_descobertas))
            print("\nChances restantes:", chances)
            print("Letras erradas:", " ".join(letras_erradas))
            
            if tentativa in letras_digitas:
                print("\nEsta letra já foi digitada. Tente Novamente!")
            elif len(tentativa) > 1:
                print("\nDigite apenas UMA letra. Tente Novamente!")
            elif tentativa.isalpha() == False:
                print("\nDigite apenas LETRAS. Tente Novamente!")
            tentativa = input("\nDigite uma letra: ").lower()
            
        if tentativa not in letras_digitas:
            letras_digitas.append(tentativa)
            
        # Condicional
        if tentativa in palavra.lower():
            index = 0

            for letra in palavra:
                if tentativa == letra.lower():
                    letras_descobertas[index] = letra
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
            print("Letras erradas:", " ".join(letras_erradas), "\n")
            break
            
    # Condicional        
    if "_" in letras_descobertas:
        limpatela()
        print(desenho_boneco(chances))
        print("\nVocê Perdeu, a palavra era", palavra, "\n")

# Bloco Main
if __name__ == "__main__":
    game()
