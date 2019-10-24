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
    x = binario_para_decimal(x)
    return (x * x) - (3 * x) + 4

def torneio(populacao, num_individuos):
    vencedor = None
    
    for i in range(num_individuos):
        individuo = random.choice(populacao) # Escolhe um indivíduo aleatoriamente para o torneio
        # Escolhe o indivíduo com a maior função objetivo dentre os escolhidos
        if (vencedor is None) or funcao_objetivo(individuo) > funcao_objetivo(vencedor):
            vencedor = individuo
        #print(individuo, funcao_objetivo(individuo))
    return vencedor

# Calcula a probabilidade e efetua a mutação caso necessário
def mutacao(individuo):
    novo_individuo = ""
    for digito in individuo:
        prob_mutacao = random.uniform(0.0,1.0)
        if (prob_mutacao < 0.01): # Probabilidade de mutação
            # Invertendo os bits
            if (digito == '1'):
                novo_individuo+='0'
            else:
                novo_individuo+='1'
        else:
            novo_individuo += digito
    return novo_individuo

def crossover(pais):
    num_pares = len(pais)//2
    nova_populacao = []
    for i in range(num_pares):
        ponto_corte = random.randint(1,4) # Posição aleatória para o corte do crossover
        prob_crossover = random.uniform(0.0,1.0)
        # Escolhe os pais
        pai_1 = random.choice(pais)
        pais.remove(pai_1)
        pai_2 = random.choice(pais)
        pais.remove(pai_2)
        #print("tentativa", i)
        #print("pais",pai_1,pai_2)
        if (prob_crossover < 0.7): # Probabilidade de ocorrer o crossover
            # Combina os cromossomos dos pais
            filho_1 = pai_1[0:ponto_corte] + pai_2[ponto_corte:]
            filho_2 = pai_2[0:ponto_corte] + pai_1[ponto_corte:]
            # Mutação
            filho_1 = mutacao(filho_1)
            filho_2 = mutacao(filho_2)            
            # Verifica se o valor dos filhos se encontra no intervalo pré-definido: [-10,10]
            valor = binario_para_decimal(filho_1)
            if (valor > 10) or (valor < -10):
                filho_1 = pai_1
            valor = binario_para_decimal(filho_2)
            if (valor > 10) or (valor < -10):
                filho_2 = pai_2
            
            #print('===crossover===')
            #print('ponto de corte: ',ponto_corte)
            nova_populacao.append(filho_1)
            nova_populacao.append(filho_2)
            #print("filhos",filho_1,filho_2,"\n")
            
        else:
            nova_populacao.append(pai_1)
            nova_populacao.append(pai_2)
    return nova_populacao 

populacao = []

# Gerando a população inicial
for i in range(30):
    x = random.randint(-10,10)
    x = '{:05b}'.format(x) # formatar o inteiro para binário com 5 dígitos
    x = x.replace('-','1')
    populacao.append(x)
print("\nPopulação inicial:\n\n", populacao, "\n")

# Condição de parada 20 gerações
for i in range(20):
    pais = []
    for j in range(30): # Quantidade de pais a serem selecionados
        pais.append(torneio(populacao,2))
    populacao.clear()
    populacao = crossover(pais)
    print( "Geração", i + 1, ":\n\n",populacao,"\n")

funcao_max = 0
x_funcao_max = 0
# Calculando a melhor solução da população resultando, ou seja, o melhor indíviduo
for x in populacao:
    if(funcao_objetivo(x) > funcao_max):
        funcao_max = funcao_objetivo(x)
        x_funcao_max = binario_para_decimal(x)

print("\nMelhor x =",x_funcao_max)
print("Função máxima =",funcao_max)
