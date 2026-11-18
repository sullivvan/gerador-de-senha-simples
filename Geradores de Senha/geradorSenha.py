import random, string

characters = string.ascii_letters + string.digits + string.punctuation
senha = "".join(random.choices(characters, k=16))

print(f"Sua nova senha: {senha}")