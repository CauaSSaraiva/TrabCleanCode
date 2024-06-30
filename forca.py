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

def exibir_classificacao():
    if not registro:
        print("\nNenhum registro encontrado.")
        return
    usuarios = []
    pontos = []
    tempos = []
    for parte in registro:
        partes = parte.split(";")
        usuarios.append(partes[0])
        pontos.append(int(partes[1]))
        tempos.append(float(partes[2]))
    merged = list(tuple(zip(usuarios, pontos, tempos)))
    ordenado = sorted(sorted(merged, key=itemgetter(2)), key=itemgetter(1), reverse=True)
    usuariosOrdenado, pontosOrdenado, temposOrdenado = zip(*ordenado)
    print("\nRanking dos usuários")
    print("-"*40)
    print("Nome do Usuário............... Pontos... Tempo")
    print
    for usuario, tempo, ponto in zip(usuariosOrdenado, temposOrdenado, pontosOrdenado):
        print(f"{usuario:30s} {ponto:<8d} {tempo:6.2f}s")

carrega_pontuacao()

while True:
    exibir_menu()
    importar_palavras("palavras.txt")
    sorteada = random.choice(palavras)
    partesSorteada = list(sorteada) 
    nova = list('_' * len(sorteada))
    partesUpper = [letra.upper() for letra in partesSorteada]

    escolha = int(input("\n Digite o n° correspondente: "))
    if escolha == 1:
        start = time.time()
        print("Escolha De Dificuldade\n")
        print("1. Jogar no nível Fácil")
        print("2. Jogar no nível Médio")
        print("3. Jogar no nível Difícil")
        print("4. Sair")
        print("="*40)
        dificuldade = input("\nEscolha uma opção: ")
        if dificuldade == "1":
            print("\nNível Fácil selecionado.")
            limiteTempo = 120
        elif dificuldade == "2":
            print("\nNível Médio selecionado.")
            limiteTempo = 60
        elif dificuldade == "3":
            print("\nNível Difícil selecionado.")
            limiteTempo = 40
        else:
            print("\nOpção inválida, padrão de Nível Médio selecionado")
            limiteTempo = 60

        nome = input("Nome do usuário: ")
        
        while True:
            tempoAtual = time.time() - start
            bonequinhoAtual = bonequinho[vidas]
            print(bonequinhoAtual, end='')   
            print(f"\n{' ' * 12}{'   '.join(nova)}\n") 
            
            if vidas <= 0:
                print("\nVish, suas vidas zeraram e você perdeu o jogo...")
                grava_pontuacao(vidas, tempoAtual)
                break
            if tempoAtual >= limiteTempo:
                print(f"Tempo esgotado! Você excedeu o limite de {limiteTempo} segundos.")
                print(f"A palavra era '{sorteada}'.")
                grava_pontuacao(vidas, tempoAtual)
                break
                
            digitado = input("Digite uma letra: ")
            acertos = 0
            for i in range(len(sorteada)):
                if partesUpper[i] == digitado.upper():
                    nova[i] = digitado.upper()
                    acertos += 1
            if acertos > 0:
                print("\nEi, você acertou uma(s) letra!\n")
            if partesUpper == nova:
                print("Você descobriu a palavra! parabéns!\n")
                print("   ".join(nova))
                grava_pontuacao(vidas, tempoAtual)
                break
            if acertos == 0:
                vidas -= 1
                print("\nOps, essa letra não está na palavra")
                print(f"\nVocê perdeu 1 vida\n Total de vidas: {vidas}")
                
    elif escolha == 2:
        exibir_classificacao()
    else:
        break