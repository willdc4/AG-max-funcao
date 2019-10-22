from funcoes import *

populacao = []
##para representar de 0 a 10 é preciso 4 bits +1 bit pra sinal
for i in range(30):
    x = random.randint(-10,10) #valor de x varia de -10 a 10
    populacao.append(x)

for i in range(20): ##20 gerações
    populacao = torneio(populacao)

##Verificar maior valor da função após 20 gerações

resultado = verifica_melhor_individuo(populacao)
x = resultado[0]
maior = resultado[1]

print('O valor de X encontrado em 20 gerações para que a função tenha valor máximo é:', x, ' e o resultado é', maior)
    
