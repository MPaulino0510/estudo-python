def porcentagem (precos, desconto = 0.1): # Temos que definir o qua nto de desconto que o usuário vai ter, no caso vai ser de 10%
    return precos * (1 - desconto) # Em vez de pegar o valor de 10% e subtrair, só subtraimos o 100% - 10% (ou seja, 1 - 0,1) e já multiplica por 90% direto 

print(porcentagem(100))
print(porcentagem(100, 0.5))


# Função para mostrar as compras
def mostrar(compras):
    for i, j in enumerate(compras, 1): 
        
        # O enumerate deixa automáticamente um desempacotamento automático nessa ordem: 1 variável = pega o índice. 2 variável = pega o item. Ou seja, quando escrevemos "enumerate()", estamos chamando: "posição, item"

        # Em outras palavras, esse código está falando: para cada parâmetro (valor que o usuário escreve), será *enumerado*, ou, organizado em ordem crescente estes, começando no parâmetro 1, ou seja, vai ir aumentando para cada valor (parâmetro) que tiver
        print(f"{i}. {j}") # Aqui escreve o número (i) e o objeto concomitante (j)

lista = [] # Criamos uma lista vazia, para depois chamar e ver ela

while True:
    i = input("Digite um item para comprar (ou sair para encerrar): ") # i Se torna o objeto que o usuário for escrever para lista

    if i.lower() == 'sair': # Se escrever "Sair", o programa encerra
        break

    lista.append(i) # É adicionado na lista, o objeto que o usuário escreveu (append adiciona no final)
    print(f"{i} foi adicionado!")

if lista:
    mostrar(lista) # Essa função mostra a lista não só por causa do "for" dentro de compras (no final, compras se torna a "lista" que o usuário escreveu), mas também, graças ao "enumerate", já é organizado em ordem crescente cada objeto da lista. O for, é para cada valor i, vai ser lido compras (ou lista)
else:
    print("Sua lista não foi preenchida")
