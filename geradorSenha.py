import random, string

caracteres = string.ascii_letters + string.digits + string.punctuation
senha = "".join(random.choice(caracteres, k=16))

print(f"Sua nova senha: {senha}")