import pandas as pd # Essa biblioteca serve para organizar os dados para a IA
from sklearn.linear_model import LinearRegression # Já este, a biblioteca que vai fazer o "Machine learn", o predict

dados = {
    'HorasEstudo': [1,2,3,4,5], # Colocamos em formato de tabela, novamente para IA ler
    'Notas': [6,7,8,9,10]
}

tabela = pd.DataFrame(dados) # Transformamos as informações dos "dados" para "DataFrame", (ou seja tabela)


entradaDadosNotas = tabela['Notas'] # Matriz. Como só possuem um colchetes ([]), são unidimensionais, ou seja, podem ser acessados com base no índice (resumindo, um array simples, linhas)
entradaDadosHoras = tabela[['HorasEstudo']] # Vetor. Como possuem dois colchetes ([[]]), bidimensional, portanto, é necessário duas informações para acessar os dados

modelo = LinearRegression()
modelo.fit(entradaDadosHoras, entradaDadosNotas) # ".fit", serve literalmente para efetuar o treinamento da IA, analisando  as duas informações

# Predict:

HorasAlunos = [[6]] # Damos um valor de horas para IA predictar a nota
predictNota = modelo.predict(HorasAlunos) # Faz o predict com base nas horas que definimos "HorasAlunos"

print(f"Se estudar 6 horas, a nota prevista será: {predictNota[0]:.1f}")