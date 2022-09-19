import secrets
import string

# Secrets é usado em preferência ao gerador de números pseudoaleatórios padrão no módulo random!!! 
# fonte: https://docs.python.org/pt-br/3/library/secrets.html

crct = string.ascii_letters + string.digits + "!@#$%¨&*\/"
# + string.ascii_lowercase + string.ascii_uppercase

senha = ''.join(secrets.choice(crct)for i in range(10))

print(senha)
