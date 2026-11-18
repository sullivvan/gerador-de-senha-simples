🔐 Gerador de Senhas em Python
📌 Sobre o projeto

Este projeto foi desenvolvido durante meus estudos de Python, com o objetivo de aprender na prática como criar um gerador de senhas aleatórias.

Durante o aprendizado, desenvolvi duas versões de um gerador de senhas, utilizando os módulos random e string do Python.

A ideia foi praticar conceitos como variáveis, funções, bibliotecas, strings e estruturas de repetição.

🚀 Primeiro código – Gerador de senha com função

Na primeira versão, desenvolvi uma função chamada gerar_senha(), responsável por criar uma senha aleatória de acordo com o comprimento informado.

Código:
python
import random, string

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = []
    for i in range(comprimento):
        caractere = random.choice(caracteres)
        senha.append(caractere)

    return ''.join(senha)

senha = gerar_senha(12)
print("Senha gerada:", senha)

Como funciona?
string.ascii_letters: disponibiliza letras maiúsculas e minúsculas.
string.digits: disponibiliza números de 0 a 9.
string.punctuation: disponibiliza caracteres especiais.
random.choice(): escolhe um caractere aleatório.
append(): adiciona o caractere à lista.
join(): transforma a lista em uma única string.
return: retorna a senha gerada.

Resultado: uma senha aleatória com 12 caracteres.

🔑 Segundo código – Gerador de senha simplificado

Na segunda versão, procurei simplificar o código utilizando random.choices() para selecionar vários caracteres aleatórios de uma só vez.

Código:
python
import random, string

characters = string.ascii_letters + string.digits + string.punctuation
senha = "".join(random.choices(characters, k=16))

print(f"Sua nova senha: {senha}")

Como funciona?
characters: reúne todas as letras, números e símbolos disponíveis.
random.choices(): seleciona vários caracteres aleatórios.
k=16: determina que a senha terá 16 caracteres.
"".join(): junta os caracteres selecionados.
print(): exibe a senha gerada.

Resultado: uma senha aleatória com 16 caracteres.

📊 Comparação entre os códigos
Característica	Primeiro código	Segundo código
Comprimento	12 caracteres	16 caracteres
Função personalizada	Sim	Não
Método aleatório	random.choice()	random.choices()
Estrutura de repetição	Sim	Não
Caracteres especiais	Sim	Sim
🧠 O que aprendi com esse projeto?

Durante o desenvolvimento, consegui praticar e compreender melhor:

Importação de bibliotecas no Python.
Utilização dos módulos random e string.
Criação e utilização de funções.
Manipulação de strings e listas.
Estruturas de repetição (for).
Utilização de métodos como choice(), choices(), append() e join().
Geração de dados aleatórios.
🎥 Materiais utilizados para estudar

Para desenvolver esse projeto, utilizei vídeos do YouTube como material de apoio e aprendizado.

Vídeos utilizados:

Primeiro vídeo: [Adicionar link do YouTube aqui]
Segundo vídeo: [Adicionar link do YouTube aqui]
Terceiro vídeo: [Adicionar link do YouTube aqui]
🛠️ Tecnologias utilizadas
Python 3
Biblioteca random
Biblioteca string
Visual Studio Code (se utilizado)
📌 Possíveis melhorias futuras
Permitir que o usuário escolha o tamanho da senha.
Criar um menu interativo.
Adicionar opções para incluir ou remover símbolos.
Utilizar o módulo secrets para gerar senhas com segurança criptográfica.
👨‍💻 Considerações finais

Esse projeto foi uma forma de colocar em prática os conhecimentos adquiridos estudando Python através de vídeos no YouTube.

Mesmo sendo um projeto simples, foi importante para entender melhor a lógica de programação e como utilizar bibliotecas para resolver problemas do dia a dia.

Pretendo continuar praticando e desenvolvendo novos projetos para aprimorar meus conhecimentos em programação.

Projeto desenvolvido para fins de estudo e aprendizado em Python. 🐍