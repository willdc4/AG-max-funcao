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

def crossover_mutacao(individuo_um, individuo_dois):

    x = random.randint(1,100)
    if(x <= 70): ##taxa de crossover

        ponto_de_corte = random.randint(1,4)

        binario_individuo_um = f'{individuo_um:05b}' # formatar o inteiro para binário com 5 dígitos
        binario_individuo_um = binario_individuo_um.replace('-','1') #se for negativo, troca o '-' por '1'

        binario_individuo_dois = f'{individuo_dois:05b}'
        binario_individuo_dois = binario_individuo_dois.replace('-','1')

        cauda_individuo_um = binario_individuo_um[ponto_de_corte:5]
        cauda_individuo_dois = binario_individuo_dois[ponto_de_corte:5]

        filho_um = binario_individuo_um[:ponto_de_corte] + cauda_individuo_dois
        filho_dois = binario_individuo_dois[:ponto_de_corte] + cauda_individuo_um

        ##Crossover finalizado

        filho_um = list(filho_um)
        filho_dois = list(filho_dois)

        for i in range(5):
            x = random.randint(1,100) ##taxa de mutacao
            if(x == 1):
                if(filho_um[i] == '0'):
                    filho_um[i] = '1'
                else:
                    filho_um[i] = '0'

        for i in range(5):
            x = random.randint(1,100)
            if(x == 1):
                if(filho_dois[i] == '0'):
                    filho_dois[i] = '1'
                else:
                    filho_dois[i] = '0'
        
        filho_um = ''.join(filho_um)
        filho_dois = ''.join(filho_dois)

        filho_um = binario_para_decimal(filho_um)
        filho_dois = binario_para_decimal(filho_dois)

        if((filho_um < -10) or (filho_um > 10) or (filho_dois < -10) or (filho_dois > 10)): ##Se filho originado não está no intervalo determinado pelo professor mantém os pais
            filho_um = individuo_um
            filho_dois = individuo_dois

    else: ##Não houve crossover, portanto os filhos são cópias idênticas aos pais
        filho_um = individuo_um
        filho_dois = individuo_dois

    return [filho_um, filho_dois]

def torneio(populacao):
    grupos = []
    grupo = []
    i = 1
    ##divisão da população em 10 grupos contendo 3 integrantes cada
    while(i < len(populacao) + 1):
        grupo.append(populacao[i - 1])
        if(i % 3 == 0):
            grupos.append(grupo)
            grupo = []
        i += 1

    nova_populacao = []
    ganhadores = []
    for grupo in grupos:
        resultado_funcoes = []
        for individuo in grupo: 
            y = funcao_de_x(individuo) ##Para cada individuo da população é verificado o valor de y
            lista = [individuo] + [y]
            resultado_funcoes.append(lista) ##Cada x (individuo) fica associado a seu valor de y
        resultado_funcoes = sorted(resultado_funcoes, key = lambda x: x[1], reverse=True) ##Ordena pelo valor de y para identificar os dois melhores individuos

        ##Realizarão o crossover posteriormente os ganhadores do torneio dois a dois
        ganhadores.append(resultado_funcoes[0][0])

        
        nova_populacao.append(resultado_funcoes[0][0])


        ##O último colocado do torneio é eliminado, o segundo colocado permanece para a próxima geração
        for i in range(1,2):
            nova_populacao.append(resultado_funcoes[i][0])

    ##Crossover e mutação
    for i in range(0, 10, 2): ##Os vencedores par a par possivelmente realizam o crossover e mutação
        individuo_um = ganhadores[i]
        individuo_dois = ganhadores[i+1]
        nova_geracao = crossover_mutacao(individuo_um, individuo_dois)
        nova_populacao += nova_geracao

    return nova_populacao

def verifica_melhor_individuo(populacao):
    maior = funcao_de_x(populacao[0])
    x = populacao[0]

    for i in range(1, len(populacao)):
        y = funcao_de_x(populacao[i])
        if(y > maior):
            maior = y
            x = populacao[i]

    return [x, maior]