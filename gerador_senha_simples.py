# Gerador de Senha Python - Formato simples, utilizando o random (menos seguro)

import string 
import random 

# variaveis

crct = string.ascii_letters 
num = string.digits 
simb = "!@#$%&*/\?" # opcional - verificar possibilidade do uso de alguns desses símbolos

aleatoriedade = crct + num + simb # elementos 
tamanho_senha = 8 # tamanho da senha

senha = "".join(random.sample(aleatoriedade, tamanho_senha))

print(senha)
