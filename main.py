'''random x
populacao inicial 30
mutacao = 0.01
crossover = 0.7
selecao por torneio
num_geracoes = 5
f(x) = (x * x) - (3 * x) + 4
'''
import random

def funcao_de_x(x):
    return (x*x) - (3*x) + 4


# Converte o valor 'x' de binário para decimal
def binario_para_decimal(x):
    x_decimal = 0
    for i in range(1,5):
        if (x[i] == '1'): # Onde houver o digito '1', somar ao valor 'x_decimal' o resultado de 2 elevado a potencia de 'i'
            x_decimal += (2 ** (4-i)) # A potência diminui da direita para a esquerda
    if (x[0] == '1'): # Quando o primeiro bit for '1' indica que 'x' é um valor negativo
        return -x_decimal
    return x_decimal

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
        print('GRUPO: ', grupos.index(grupo))
        for individuo in grupo:
            y = funcao_de_x(individuo)
        
            
            
        
    #print(grupos)


populacao = []
##para representar de 0 a 10 é preciso 4 bits 
for i in range(30):
    x = random.randint(-10,10) #valor de x varia de -10 a 10
    #x = f'{x:05b}' # formatar o inteiro para binário com 5 dígitos
    #x = x.replace('-','1')
    populacao.append(x)

torneio(populacao)
