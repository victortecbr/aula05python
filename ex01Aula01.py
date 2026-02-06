# Escreva um algoritmo em Python que leia uma opção escolhida pelo usuário e faça as 
# seguintes rotinas:
# 1 – escolha um número diga se é par ou ímpar
# 2 – escolha dois valores e diga quem é o maior entre eles ou se são iguais.
# 3 – escolha um valor e calcule o dobro mostrando para o resultado para o usuário.
# Implemente a estrutura WHILE para decidir quantas vezes o usuário vai testar a aplicação

opcao = 0

while opcao != 4:
    print("\n===== MENU =====")
    print("1 - Verificar se um número é par ou ímpar")
    print("2 - Comparar dois valores")
    print("3 - Calcular o dobro de um valor")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        numero = int(input("Digite um número: "))
        if numero % 2 == 0:
            print("O número é PAR.")
        else:
            print("O número é ÍMPAR.")

    elif opcao == 2:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))

        if valor1 > valor2:
            print(f"O maior valor é: {valor1}")
        elif valor2 > valor1:
            print(f"O maior valor é: {valor2}")
        else:
            print("Os dois valores são IGUAIS.")

    elif opcao == 3:
        valor = float(input("Digite um valor: "))
        dobro = valor * 2
        print(f"O dobro do valor é: {dobro}")

    elif opcao == 4:
        print("Encerrando o programa... 👋")

    else:
        print("Opção inválida! Escolha uma opção entre 1 e 4.")