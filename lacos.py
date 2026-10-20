# Neste código, é contado de 0 até 4
for i in range(5):
    print(f"Número {i}")

# Neste, contará de 0 até o (supostamente) 11, contando de 2 em 2, no caso específico o 11 não consegue aparecer
for pares in range(0, 11, 2):
    print(pares)

#Já neste, só os ímpares são imprimidos no terminal (começa com 1)
for impares in range(1, 11, 2):
    print(impares)

# Observação: cuidado ao escrever esses laços, se estiver um debaixo do outro com um formato específico, isso pode gerar alguns erros de síntase (de impressão) ou pode servir para outras coisas

# Neste caso, enquanto as tentativas forem menores que 10, será escrito "Tentativa N°", e sempre somando as tentativas, caso chegue no 10, pare o comando
tentativas = 0

while tentativas <= 10:
    print(f"Tentativa N°{tentativas}")
    tentativas += 1

print("Fim de tentativas")


while True:
    resposta = input("Digite 'sair' para encerrar o programa: ")
    if resposta.lower() == "sair":
        print("Saindo...")
        break
    print(f"Você digitou {resposta}")
