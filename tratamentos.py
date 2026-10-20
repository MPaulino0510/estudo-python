# Esse código abaixo dá erro se o usuário digitar uma letra (como "dez"), por isso iremos tratar esse erro com try e except
# idade = int(input("Digite sua idade: "))

# Correto para tratamento de erros:

while True:
    try: # Neste caso, ele tenta trocar string para int:
        idade = int(input("Escreva sua idade: "))
        print(f"Você possui {idade} anos.")
        break
    except ValueError: # Se der erro ao escrever int:
        print("Número digitado de forma incorreta. Tente novamente.")

# Outro caso:

while True:
    try:
        numero1 = float(input("Escreva o dividendo: "))
        numero2 = float(input("Escreva o divisor: "))
        resultado = numero1 / numero2
    except ValueError:
        print("Erro de digitação. Tente novamente.")
    except ZeroDivisionError: # Se for dividido por 0
        print("Não é possível dividir por zero!")
    else:
        print(f"Resultado: {resultado}")
    while True:
        resposta = input("Deseja continuar calculando (S/N)?").strip().upper() # O strip serve para remover espaços em branco, já o upper para deixar tudo em letra maiúscula
        if resposta == "S":
            break
        elif resposta == "N":
            print("Programa encerrado.")
            exit()
        else:
            print("Erro de digitação! Digite (S/N) apenas")
        
