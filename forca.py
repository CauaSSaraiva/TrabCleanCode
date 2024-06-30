import random
import os
import time
from operator import itemgetter

# Listas e variáveis
palavras = [] 
registro = []
vidas = 6

bonequinho = [
"""
                _________
                |/      |
                |       O
                |     --|--
                |       |
                |      / \\
            ____|_\\___
""",
"""
                _________
                |/      |
                |       O
                |     --|--
                |       |
                |      /
            ____|_\\___
""",
"""
                _________
                |/      |
                |       O
                |     --|--
                |       |
                |
            ____|_\\___
""",
"""
                _________
                |/      |
                |       O
                |     --|
                |       |
                |
            ____|_\\___
""",
"""
                _________
                |/      |
                |       O
                |       |
                |       |
                |
            ____|_\\___
""",
"""
                _________
                |/      |
                |       O
                |
                |
                |
            ____|_\\___
""",
"""
                _________
                |/      |
                |
                |
                |
                |
            ____|_\\___
"""
]

def verificacao_vidas(vidas):
    if vidas <= 0:
        print("\nVish, suas vidas zeraram e você perdeu o jogo...")
        return True

def verificacao_vitoria():
    if partesUpper == partesAtual:
        print("Você descobriu a palavra! parabéns!\n")
        print("   ".join(partesAtual))
        return True
    else:
        return False

def verificacao_acerto(digitado):
     for i in range(len(sorteada)):
        acertos = 0
        if partesUpper[i] == digitado.upper():
           partesAtual[i] = digitado.upper()
           acertos += 1
        if (i + 1) == len(sorteada) and acertos > 0:
           print("\nEi, você acertou uma(s) letra!\n")
           return True

def verificacao_erro(digitado):
    erros = 0
    for x in range(len(sorteada)):
        if partesUpper[x] != digitado.upper():
            erros += 1
            if erros == len(sorteada):
                return True

#Cauã
def verificacao_limiteTempo(tempoAtual):
    if tempoAtual >= limiteTempo:
        print(f"Tempo esgotado! Você excedeu o limite de {limiteTempo} segundos.")
        print(f"A palavra era '{sorteada}'.")
        return True


def importar_palavras(txt):
    with open(txt, 'r') as file:
        for linha in file:
            palavra = linha.strip()
            palavras.append(palavra)

def grava_pontuacao(num, time):
    registro.append(f"{nome};{num};{time}\n")
    with open("score.txt", "w") as arq:
        for linha in registro:
            partes = linha.split(";")
            arq.write(f"{partes[0]};{partes[1]};{partes[2]}")

def carrega_pontuacao():
    if not os.path.isfile("score.txt"):
        return
    with open("score.txt", "r") as arq:
        dados = arq.readlines()
        for linha in dados:
            partes = linha.split(";")
            registro.append(f"{partes[0]};{partes[1]};{partes[2]}")

def exibir_menu():
    print("="*60)
    print("1. Iniciar novo jogo")
    print("2. Exibir placar de pontuação dos usuarios")
    print("3. Sair")
    print("="*60)

# Cauã
def escolherDificuldade():
    print("Escolha De Dificuldade\n")
    print("1. Jogar no nível Fácil")
    print("2. Jogar no nível Médio")
    print("3. Jogar no nível Difícil")
    print("4. Sair")
    print("="*40)
    escolha = input("\nEscolha uma opção: ")

    if escolha == "1":
            print("\nNível Fácil selecionado.")
            return 120
    elif escolha == "2":
            print("\nNível Médio selecionado.")
            return 60
    elif escolha == "3":
            print("\nNível Difícil selecionado.")
            return 40
    else:
            print("\nOpção inválida, padrão de Nível Médio selecionado")
            return 60

#Leonardo
def exibir_classificacao():
    if not registro:
        print("\nNenhum registro encontrado.")
        return

    usuarios = []
    for linha in registro:
        partes = linha.split(";")
        usuarios.append({"nome": partes[0], "pontos": int(partes[1]), "tempo": float(partes[2])})

    usuarios_ordenados = sorted(usuarios, key=lambda x: (-x["pontos"], x["tempo"]))

    print("\nRanking dos usuários")
    print("-"*40)
    print("Nome do Usuário............... Pontos... Tempo")
    for usuario in usuarios_ordenados:
        print(f"{usuario['nome']:30s} {usuario['pontos']:<8d} {usuario['tempo']:6.2f}s")
#Geancarlo
def jogo(vidas):
        while True:
            tempoAtual = time.time() - start
            bonequinhoAtual = bonequinho[vidas]
            print(bonequinhoAtual, end='')   
            print(f"\n{' ' * 12}{'   '.join(partesAtual)}\n") 

            if verificacao_vidas(vidas):
                grava_pontuacao(vidas, tempoAtual)
                break
            if tempoAtual >= limiteTempo:
                print(f"Tempo esgotado! Você excedeu o limite de {limiteTempo} segundos.")
                print(f"A palavra era '{sorteada}'.")
            if verificacao_limiteTempo(tempoAtual):
                grava_pontuacao(vidas, tempoAtual)
                break

            digitado = input("Digite uma letra: ")
            verificacao_acerto(digitado)
            if verificacao_vitoria():
                grava_pontuacao(vidas, tempoAtual)
                break
            if verificacao_erro(digitado):
                vidas -= 1
                print("\nOps, essa letra não está na palavra")
                print(f"\nVocê perdeu 1 vida\n Total de vidas: {vidas}")
                    

carrega_pontuacao()

while True:
    exibir_menu()
    importar_palavras("palavras.txt")
    sorteada = random.choice(palavras)
    partesSorteada = list(sorteada) 
    partesAtual = list('_' * len(sorteada))
    partesUpper = [letra.upper() for letra in partesSorteada]

    escolha = int(input("\n Digite o n° correspondente: "))
    if escolha == 1:
        start = time.time()
        limiteTempo = escolherDificuldade()

        nome = input("Nome do usuário: ")
        jogo(vidas)
        
    elif escolha == 2:
        exibir_classificacao()
    else:
        break
