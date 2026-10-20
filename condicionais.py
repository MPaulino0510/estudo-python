idade = input("Digite sua idade: ")
idadeINT = int(idade)
if idadeINT < 18:
    print("Você não é maior de idade")
elif idadeINT > 18:
    print("Você é maior de idade")
else:
    print("Você tem exatamente 18 anos")
# Este é um modo de fazer condição com operador lógicos no python, (else if)
dia = input("Digite de 1 até 7 os dias da semana: ")
if dia == "6" or dia == "7":
    print("É fim de semana!")
else:
    print("Dia de semana")
# Variável ou, nem é preciso explicar

dinheiro = False
if not dinheiro:
    print("Não possui dinheiro")
# Se não for verdadeiro, faça isso

