print("um programa para calcular o determinante de uma matriz 2x2")
print()

matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(float(input(f"elemento [{i}][{j}]: ")))
    matriz.append(linha)

a, b = matriz[0]
c, d = matriz[1]
det = a * d - b * c

print(f"o determinante é igual a {det}")