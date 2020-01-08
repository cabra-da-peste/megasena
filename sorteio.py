import random

print('*' * 40)
print('Bem-vindo ao apostador jogos da CAIXA')
print('*' * 40)
print('Selecione o jogo: ')
print('1 - mega-sena  |  2 - quina  |  3 - lotofácil  |  4 - lotomania')

op = int(input('>>>'))


tipo_jogo = ['Mega-sena', 'Quina', 'Lotofácil', 'Lotomania']
amplitude = [60, 80, 25, 100]
quantidade_numeros = [6, 5, 15, 50]

jogo = []
while quantidade_numeros[op - 1] > len(jogo):
    numero = random.randint(1, amplitude[op - 1])
    if numero not in jogo:
        jogo.append(numero)

jogo.sort()

print('Seu jogo {}'.format(tipo_jogo[op - 1]))
print(jogo)
