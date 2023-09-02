# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

import os # Importando biblioteca para limpar a tela

################################ FUNÇÕES ################################

def limpatela(): return os.system("cls")
    
#########################################################################

def tMenu(): #Tela de Opções

    print("\n===================== CALCULADORA EM PYTHON =====================")
    print("")
    print("                            [1] SOMA")
    print("                            [2] SUBTRAÇÃO")
    print("                            [3] MULTIPLICAÇÃO")
    print("                            [4] DIVISÃO")
    print("                            [5] POTÊNCIA")
    print("")
    opc = int(input("Opção: "))
    return opc

#########################################################################

def Calculadora(num1, num2, opc): # Soma
   
    if opc == 1:
       operador = "+"
       result = num1 + num2 # Retorna a Soma
    elif opc == 2:
       operador = "-"
       result = num1 - num2 # Retorna a Subtração
    elif opc == 3:
       operador = "x"
       result = num1 * num2 # Retorna a Multiplicação
    elif opc == 4:
       operador = "/"
       result = num1 / num2 # Retorna a Divisão
    elif opc == 5:
       operador = "^"
       result = num1 ** num2 # Retorna a Potência
    
    return print(num1, operador, num2, '=', result)

################################ CÓDIGO #################################
resp = "S"

while resp == "S" or resp == "SIM":
    
    limpatela()

    opc_Operacao = tMenu() #Cria a tela de Opções
    
    print("")
    
    if opc_Operacao >= 1 and opc_Operacao <= 5:  
        
        num1 = int(input("1° Número: "))
        print("")
        num2 = int(input("2° Número: "))
        
        print("")

        result = Calculadora(num1, num2, opc_Operacao)
    
    else:
        
        print("< Opção Inválida >")
    
    print("")
    
    resp = input("Deseja fazer outra Operação? [S/N]: ")
    
    resp = resp.upper()

limpatela()

print("Fechando Calculadora....")

print("")