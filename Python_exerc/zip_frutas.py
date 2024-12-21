# Criando duas listas: frutas e cores
frutas = ["maçã", "banana", "uva"]
cores = ["vermelha", "amarela", "roxa"]

# Usando zip para combinar as listas e convertendo para uma lista imediatamente
resultado = list(zip(frutas, cores))

# Exibindo a lista combinada (se necessário)
print("Lista combinada de frutas e cores:")
print(resultado)

# Iterando sobre a lista gerada pelo zip
print("\nDetalhando cada par:")
for fruta, cor in resultado:
    print(f"A {fruta} é {cor}.")

# O zip() no Python é uma função embutida que combina elementos de duas ou mais sequências (como listas, tuplas, ou outras iteráveis), formando pares ou grupos.
# O nome zip vem da ideia de um zípper (fecho de zíper), que junta dois lados em pares. Vamos explorar isso com exemplos simples!