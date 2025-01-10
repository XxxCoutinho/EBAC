# Calculadora Simples

# Inicializando variáveis
valor1 = 0
valor2 = 0
operacao = 0
resposta = 0
cont_cal = "s"
soma = "+"
subtracao = "-"
divisao = "/"
multiplicacao = "*"

print("Olá, esse é um projeto de calculadora em desenvolvimento, se atente às orientações!\n")

print("Para utilizar essa calculadora:")
print("- Informe um número e aperte 'Enter'")
print("- Escolha uma operação (+, -, /, *) e aperte 'Enter'")
print("- Informe o segundo número e aperte 'Enter' novamente")
print("- Aguarde enquanto o cálculo é realizado!\n")
print("Vamos começar!!!")

# Loop para realizar cálculos continuamente
while cont_cal == "s":

    print("")
    try:
        valor1 = float(input("Informe o primeiro valor que deseja calcular: "))
        operacao = input("Informe a operação que deseja realizar (+, -, /, *): ")
        valor2 = float(input("Informe o segundo valor que deseja calcular: "))

        if operacao == soma:
            resposta = valor1 + valor2
            print(f"{valor1} + {valor2} = {resposta}\n")

        elif operacao == subtracao:
            resposta = valor1 - valor2
            print(f"{valor1} - {valor2} = {resposta}\n")

        elif operacao == divisao:
            if valor2 != 0:
                resposta = valor1 / valor2
                print(f"{valor1} / {valor2} = {resposta}\n")
            else:
                print("Erro: divisão por zero não é permitida.\n")

        elif operacao == multiplicacao:
            resposta = valor1 * valor2
            print(f"{valor1} * {valor2} = {resposta}\n")

        else:
            print("\nOperação inválida! Tente novamente usando +, -, / ou *.\n")

    except ValueError:
        print("\nErro: Certifique-se de inserir números válidos.\n")

    cont_cal = input("Deseja realizar outro cálculo? (s/n): ").lower()

    if cont_cal == "n":
        print("\nObrigada por utilizar nossos serviços, até a próxima!")
        break
