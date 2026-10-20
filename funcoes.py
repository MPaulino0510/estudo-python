# Realizando funções:
def cumprimentar(nome):
    print(f"Olá, {nome}! Seja bem vindo.")

nome = input("Escreva seu nome: ")
cumprimentar(nome)
# Uma função simples, cuja função gira em torno da variável "nome"

numero1Txt = input("Escreva um número: ")
numero2Txt = input("Escreva outro número: ")

numero1 = int(numero1Txt)
numero2 = int(numero2Txt)


operador = input("Escreva um operador para realizar os cálculos: ")
def operacoes (a, b):
    if operador == "+":
        resultado = a+b
        return resultado
    elif operador == "-":
        resultado = a-b
        return resultado
    elif operador == "*":
        resultado = a*b
        return resultado
    elif operador == "/":
        resultado = a/b
        return resultado
    else:
        print("Opção inválida")
total = operacoes(numero1, numero2)
print(f"O resultado dessa operação é: {total}")

