import random, string

characters = string.ascii_letters + string.digits + string.punctuation
senha = "".join(random.choices(characters, k=16))

print(f"Sua nova senha: {senha}")

# Gerador de senha aleatória
    #Letras = string.ascii_letters
    #Números = string.digits
    #Símbolos = string.punctuation

    #Quantidade de caracteres da senha = k=Número de caracteres desejados

    #Aprendizado na prática
    #Video utilizado: https://www.youtube.com/watch?v=j3NTeX4w8YA