#Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação 
#e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
#1. Soma
#2. Subtração
#3. Multiplicação
#4. Divisão
#Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def calculadora (numero1, numero2, operacao):

    if(operacao == 1):
        return numero1 + numero2
    
    elif(operacao == 2):
        return numero1 - numero2
    
    elif (operacao == 3):
        return numero1 * numero2
    
    elif (operacao == 4):
        return numero1 / numero2
    
    else:
        return 0
    
resultado = calculadora (2, 3 ,1)
print(resultado)