# Versão 0.3
from random import randint

# Validação input numeros
while True:
    try:
        n_numeros = int(input("Informe quantos numeros: "))
        if n_numeros < 6 or n_numeros > 15:
            raise ValueError()
        break
    except ValueError:
        print("Você deve inserir um valor inteiro entre 6 e 15")

# Validação input quantidade de jogos
while True:
    try:
        n_jogos = int(input("Informe a quantidade de jogos "))
        if n_jogos < 1 or n_jogos > 10:
            raise ValueError()
        break
    except ValueError:
        print("Você deve inserir um valor inteiro entre 1 e 10.")
'''
#Definição função números com maior frequencia
def maior_frequencia(n_numeros, n_jogos):
    for x in range(n_jogos):
        print("--------------------------------------")
        print("jogo", x + 1)
        jogo = []
        teste = dfMS['1ª Dezena'].value_counts().head(n_numeros).get
        while len(jogo) != n_numeros: #enquanto o tamanho da lista não for igual a quantidade de números informados repetir a operação
            r = randint(1,60) #r recebe um número aleatório entre 1 e 60
            if r not in jogo: #Se r não existir na lista acrescentá-lo
              jogo.append(r) 

        print(sorted(teste)) #imprimir número ordenado

'''


# Definição função megasena
def megasena(n_numeros, n_jogos):
    for x in range(n_jogos):
        print("--------------------------------------")
        print("jogo", x + 1)
        jogo = []
        while len(
                jogo) != n_numeros:  # enquanto o tamanho da lista não for igual a quantidade de números informados repetir a operação
            r = randint(1, 60)  # r recebe um número aleatório entre 1 e 60
            if r not in jogo:  # Se r não existir na lista acrescentá-lo
                jogo.append(r)

        print(sorted(jogo))  # imprimir número ordenado


'''
#Define valor do jogo utilizando if e elif

def valorjogo(n_numeros, n_jogos):
    if n_numeros == 6:
        ValorPorJogo = 4.50
    elif n_numeros == 7:
        ValorPorJogo = 31.50
    elif n_numeros == 8:
        ValorPorJogo = 126
    elif n_numeros == 9:
        ValorPorJogo = 378
    elif n_numeros == 10:
        ValorPorJogo = 945        
    elif n_numeros == 11:
        ValorPorJogo = 2079
    elif n_numeros == 12:
        ValorPorJogo = 4158        
    elif n_numeros == 13:
        ValorPorJogo = 7722        
    elif n_numeros == 14:
        ValorPorJogo = 13513.50        
    elif n_numeros == 15:
        ValorPorJogo = 13513.50

    ValorTotalJogo = ValorPorJogo * n_jogos
    return ValorTotalJogo
'''


# Define valor do jogo utilizando um dicionário
def valorjogo1(n_numeros, n_jogos):
    dicValor = {6: 4.50, 7: 31.50, 8: 126, 9: 378, 10: 945, 11: 2079, 12: 4158, 13: 7722, 14: 13513.50, 15: 13513.50}
    ValorPorJogo = dicValor[n_numeros]
    ValorTotalJogo = ValorPorJogo * n_jogos
    return ValorTotalJogo


# Função que mostra a probabilidade pela quantidade de números
def probabilidade(n_numeros):
    probSena = {6: "50.063.860", 7: "7.151.980", 8: "1.787.995", 9: "595.998", 10: "238.399", 11: "108.363",
                12: "54.182", 13: "29.175", 14: "16.671", 15: "10.003"}
    probQuina = {6: 154.518, 7: 44.981, 8: 17.192, 9: 7.791, 10: 3.973, 11: 2.211, 12: 1.317, 13: 828, 14: 544, 15: 370}
    probQuadra = {6: 2.332, 7: 1.038, 8: 539, 9: 312, 10: 195, 11: 129, 12: 90, 13: 65, 14: 48, 15: 37}
    ProbabilidadeJogo = (probSena[n_numeros], probQuina[n_numeros], probQuadra[n_numeros])
    return ProbabilidadeJogo


# chama a função megasena passando a quantidade de números e quantidade de jogos
megasena(n_numeros, n_jogos)
# maior_frequencia(n_numeros, n_jogos)
print("\n O valor total dos jogos é R$ ", valorjogo1(n_numeros, n_jogos))

print("\n Probabilidade de acerto de acerto apostando ",n_numeros," dezenas por jogo é de SENA: 1 em ",probabilidade(n_numeros)[0]," QUINA: 1 em ",probabilidade(n_numeros)[1]," QUADRA: é  1 em ",probabilidade(n_numeros)[2])