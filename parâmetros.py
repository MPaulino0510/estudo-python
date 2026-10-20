def porcentagem (precos, desconto = 0.1): # Temos que definir o qua nto de desconto que o usuário vai ter, no caso vai ser de 10%
    return precos * (1 - desconto) # Em vez de pegar o valor de 10% e subtrair, só subtraimos o 100% - 10% (ou seja, 1 - 0,1) e já multiplica por 90% direto 

print(porcentagem(100))
print(porcentagem(100, 0.5))
