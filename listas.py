# Fazendo arrays
objetos = ["Lápis", "Apontador", "Borracha"]

# Printando códigos, quando se escreve um valor negativo, ele conta de trás para frente
print(objetos[2])
print(objetos[-1])

# Adiciona ao final
objetos.append("Caneta")

# Para editar um objeto que já existe numa array, basta chamar o valor dele dentro da array, e escrever oque foi alterado
objetos[2] = "Branquinho"

# Remove uma array
objetos.remove("Lápis")

# Escreve o nome de todos array
print(objetos)

# Escreve o total de objetos dentro do array
print(f"Total de objetos: {len(objetos)}")