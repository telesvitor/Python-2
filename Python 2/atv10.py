boletim = {}
while True:
    nome = input("Digite o nome do aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
        boletim[nome] = nota
    continuar = input("Deseja adicionar outro aluno? [S/N]: ").strip().upper()
    if continuar != 'S':
        break
print("\n--- Resultados do Boletim ---")
for nome, nota in boletim.items():
    if nota >= 6.0:
        status = "Aprovado"
    else:
        status = "Reprovado"
    print(f"O(a) aluno(a) {nome} tirou {nota} e está {status}.")
