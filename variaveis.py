# Como declarar a variável em python, semelhante ao javascript.

nome = "Miguel" # classe str (string)
possuiDinheiro = True # classe boolean
altura = 1.65 # classe float
carros = 3 # classe int

print(nome) # Como se escreve no python

print(type(nome)) # Aqui mostra o tipo das classes da variável
print(type(possuiDinheiro))

Miguel, Ana, Joao = 10, 20, 30 # No python, é possível declarar variáveis, de acordo com a ordem delas

print(Ana)

Carlos = Felipe = Professor = 0 # Todas variáveis de nomes valerão 0

print(Carlos, Professor)

Thiago = Nicolas = 1
print(Nicolas)

print(f"Olá {nome}, seja bem vindo!") # O f serve para chamar as variáveis

texto = "100"
print(type(texto))
numeroDoTexto = int(texto) # Quando se coloca o tipo de valor a uma variável, é possível  converter seu tipo para qualquer outro. Este método é chamado de Casting
print(type(numeroDoTexto))

nomeUsuario = input("Digite seu nome: ") # O input permite que o usuário escreva suas informações no terminal
idadeUsuario = input("Digite sua idade: ")
idadeInt = int(idadeUsuario)
