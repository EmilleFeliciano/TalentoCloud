import datetime

def obter_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (1922-2021): "))
            if 1922 <= ano_nascimento <= 2021:
                return ano_nascimento
            else:
                print("Por favor, digite um ano entre 1922 e 2021.")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

def main():
    nome_completo = input("Digite seu nome completo: ")
    ano_nascimento = obter_ano_nascimento()

    idade = calcular_idade(ano_nascimento)

    print(f"\nOlá, {nome_completo}!")
    print(f"Você completa ou já completou {idade} anos em 2022.")

if __name__ == "__main__":
    main()