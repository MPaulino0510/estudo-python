numeros = {1,2,2,3,4,5,5,5,5} # Ignora os números repetidos
print(numeros)

letrasDuplicadas = ["a", "a", "a", "b", "c", "d", "d"]
letrasNaoRepetidas = list(set(letrasDuplicadas)) # "Limpa" as letras repetidas, mas não mantém a ordem orginal delas
print(letrasNaoRepetidas)

letrasOrganizadas = list(dict.fromkeys(letrasDuplicadas)) # "Limpa" as letras repetidas, e mantém a ordem original delas

print(letrasOrganizadas)

# Outra maneira de eliminar letras repetidas, e deixar na ordem
listas = ["f", "y", "z", "z"]
ordenados = [] # Cria um array sem nenhuma informação ainda, iremos colocar informação nela ao decorrer do código

for a in listas:
    if a not in ordenados:
        ordenados.append(a) # Em outras palavras: se não houver essa letra (la na listas), adicione ela dentro do array vazio que criamos, caso contrário, continue a adicionar as outras letras que ainda não apreceram, isso ignora as repetidas

print(ordenados)