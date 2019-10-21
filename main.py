'''random x
populacao inicial 30
mutacao = 0.01
crossover = 0.7
selecao por torneio
num_geracoes = 5
f(x) = (x * x) - (3 * x) + 4
'''
import random

# Converte o valor 'x' de binário para decimal
def binario_para_decimal(x):
    x_decimal = 0
    for i in range(1,5):
        if (x[i] == '1'): # Onde houver o digito '1', somar ao valor 'x_decimal' o resultado de 2 elevado a potencia de 'i'
            x_decimal += (2 ** (4-i)) # A potência diminui da direita para a esquerda
    if (x[0] == '1'): # Quando o primeiro bit for '1' indica que 'x' é um valor negativo
        return -x_decimal
    return x_decimal

#Função objetivo do problema
def funcao_objetivo(x):
    x = int(x)
    return (x * x) - (3 * x) + 4

def torneio(populacao):
    aptidao = []
    for x in populacao:
        aptidao.append(funcao_objetivo(binario_para_decimal(x)))
    #print(aptidao)
'''
def crossover(populacao):
'''
populacao = []

for i in range(30):
    x = random.randint(-10,10)
    x =f'{x:05b}' # formatar o inteiro para binário com 5 dígitos
    x = x.replace('-','1')
    populacao.append(x)

print(populacao)
torneio(populacao)
