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

# Função Principal
def game():

    limpatela()
    
    print("\nBem-Vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    # Lista de palavras para o jogo
    palavras = ['Banana', 'Uva', 'Morango', 'Laranja', 'Abacate', 'manga']
   
    # Escolhe aleatoriamente uma palavra
    palavra = random.choice(palavras) 
    
    # List comprehension
    qtd_= ['_' for letra in palavra]

    # Número de chances
    chances = 6

    # Lista de palavras erradas
    letras_erradas = []

game()