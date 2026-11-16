print("programa para fazer a soma de duas matrizes 4x3")
print()

def ler_matriz(nome):
    m = []
    print(f"Matriz {nome}:")
    for i in range(4):
        linha = []
        for j in range(3):
            linha.append(float(input(f"  [{i}][{j}]: ")))
        m.append(linha)
    return m

A = ler_matriz("A")
B = ler_matriz("B")

C = [[A[i][j] + B[i][j] for j in range(3)] for i in range(4)]

print("matriz soma:")
print("-" * 30)
for linha in C:
    print(" | ".join(f"{valor:8.2f}" for valor in linha))
    print("-" * 30)