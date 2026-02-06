# Escreva um algoritmo em Python que leia e escreva na tela a entrada de um nome e duas
# provas. Calcule sua média. Mostre ao usuário se ele está aprovado ou reprovado com
# parâmetro de média maior ou igual a 6.0. Implemente a estrutura while para mostrar ao
# usuário que ele só pode usar os valores das provas entre 0.0 e 10.0:

# Leitura do nome do aluno
nome = input("Digite o nome do aluno: ")

# Leitura da primeira prova com validação
while True:
    prova1 = float(input("Digite a nota da primeira prova (0.0 a 10.0): "))
    if 0.0 <= prova1 <= 10.0:
        break
    else:
        print("Nota inválida! Digite um valor entre 0.0 e 10.0.")

# Leitura da segunda prova com validação
while True:
    prova2 = float(input("Digite a nota da segunda prova (0.0 a 10.0): "))
    if 0.0 <= prova2 <= 10.0:
        break
    else:
        print("Nota inválida! Digite um valor entre 0.0 e 10.0.")

# Cálculo da média
media = (prova1 + prova2) / 2

# Exibição do resultado
print(f"\nAluno: {nome}")
print(f"Média: {media:.2f}")

if media >= 6.0:
    print("Situação: Aprovado ✅")
else:
    print("Situação: Reprovado ❌")


'''qnt = 1
nome = input("Digite nome do aluno.")
prova = float(input(f"Digite a nota da {qnt}° prova: "))

while prova >= 0 and prova <= 10:
    qnt <= 2:
    prova += prova
    qnt += 1
    if qnt == 2:
        media = prova / qnt
        media >= 6:
        print("Aprovado")
        print("Reprovado")'''

        
    
