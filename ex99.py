print("programa que solicita a idade e o nome de 10 pessoas e apresenta em 2 grupos: ")
print()

pessoas = []
for i in range(10):
    nome = input(f"Nome da pessoa {i+1}: ")
    idade = int(input(f"Idade de {nome}: "))
    pessoas.append((nome, idade))

menores = [p for p in pessoas if p[1] < 18]
maiores = [p for p in pessoas if p[1] >= 18]

print("menores de 18 anos:")
for nome, idade in menores:
    print(f"{nome} - {idade} anos")

print("maiores de 18 anos:")
for nome, idade in maiores:
    print(f"{nome} - {idade} anos")