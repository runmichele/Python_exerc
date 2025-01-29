def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:  # Evita divisão por zero
        return a / b
    else:
        return "Erro: Divisão por zero não é permitida!"

def exibir_menu():
    print("\nEscolha uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

# Loop principal da calculadora
while True:
    exibir_menu()
    escolha = input("Digite o número da operação desejada: ")

    if escolha == "5":
        print("Calculadora encerrada. Até mais!")
        break

    if escolha in ["1", "2", "3", "4"]:
        try:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))

            if escolha == "1":
                print(f"Resultado: {soma(numero1, numero2)}")
            elif escolha == "2":
                print(f"Resultado: {subtracao(numero1, numero2)}")
            elif escolha == "3":
                print(f"Resultado: {multiplicacao(numero1, numero2)}")
            elif escolha == "4":
                print(f"Resultado: {divisao(numero1, numero2)}")
        except ValueError:
            print("Erro: Por favor, digite números válidos.")
    else:
        print("Opção inválida. Tente novamente!")
