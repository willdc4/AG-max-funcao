'''random x
populacao inicial 30
mutacao = 0.01
crossover = 0.7
selecao por torneio
num_geracoes = 5
f(x) = (x * x) - (3 * x) + 4
'''
import random

populacao = []

def torneio(populacao):
    grupos = []
    grupo = []
    i = 1
    ##divisão da população em 5 grupos contendo 6 integrantes
    while(i < len(populacao) + 1):
        grupo.append(populacao[i - 1])
        if(i % 6 == 0):
            grupos.append(grupo)
            grupo = []
        i += 1

    for grupo in grupos:
        
    print(grupos)


##para representar de 0 a 10 é preciso 4 bits 
for i in range(30):
    x = random.randint(-10,10) #valor de x varia de -10 a 10
    x = f'{x:05b}' # formatar o inteiro para binário com 5 dígitos
    x = x.replace('-','1')
    populacao.append(x)



torneio(populacao)
