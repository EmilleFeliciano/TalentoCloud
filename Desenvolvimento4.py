#Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação 
#e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
#1. Soma
#2. Subtração
#3. Multiplicação
#4. Divisão
#Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def calculadora():
    while True:
        print("Escolha uma operacao:")
        print("1: Soma")
        print("2: Subtracao")
        print("3: Multiplicacao")
        print("4: Divisao")
        print("0: Sair")

        escolha = input("Digite um numero: ")

        if escolha == "0":
            print("Fechando calculadora.")
            break
        elif escolha in ["1", "2", "3", "4"]:
            try:
                num1 = int(input("Digite o primeiro valor: "))
                num2 = int(input("Digite o segundo valor: "))
            except ValueError:
                print("Por favor, insira valores numéricos válidos.")
                continue

            if escolha == "1":
                resultado = num1 + num2
                print(f"Resultado: {resultado}")
            elif escolha == "2":
                resultado = num1 - num2
                print(f"Resultado: {resultado}")
            elif escolha == "3":
                resultado = num1 * num2
                print(f"Resultado: {resultado}")
            elif escolha == "4":
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"Resultado: {resultado}")
                else:
                    print("Não é possível dividir por zero.")
        else:
            print("Essa opção não existe. Tente novamente.")

if __name__ == "__main__":
    calculadora()