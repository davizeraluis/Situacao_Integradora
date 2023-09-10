'''
Algoritmo calculo_lancamento_obliquo_por_metodo_de_newton
Situação Integradora EsPCEx 11/08/2023
7º Pelotão - Turma B2
Grupo 1
6153 Barreto
7035 Zefiro
7230 Rezende Silva
7245 Rocha Oliveira
7335 Pasquali
7804 Maria Júlia
7832 Vitória Gomes
'''
#Bibliotecas
#Biblioteca 'math' é necessária para usar as funções 'tan', 'radians', 'cos' e 'log'
import math

#Entrada de Dados
#Entrada dos parâmetros da função
angulo_lancamento=float(input("Digite o ângulo de lançamento (em graus): "))
velocidade_inicial=float(input("Digite a velocidade incial (em m/s): "))
gravidade=float(input("Digite o valor da gravidade (em m/s^2): "))
altura_inicial=float(input("Digite a altura inicial do lançamento (em m): "))
coeficiente_arrasto=float(input("Digite o coeficiente de arrasto (s^-1): "))

#Entrada do parâmetros do método de newton
#a função comentada a seguir calcula o valor ideal para o valor inicial
#valor_inicial=(velocidade_inicial**2)*math.sin(math.radians(2*coeficiente_arrasto))/((2*math.sin(math.radians(coeficiente_arrasto))*coeficiente_arrasto*velocidade_inicial+gravidade))
valor_inicial=float(input("Digite um valor inicial aproximado para o alcance (em m): "))
numero_iteracoes=int(input("Digite o número de iterações desejadas: "))

#A estrutura de repetição 'for' será repetida o tanto de vezes que o usuário digitar
for i in range (1,numero_iteracoes):
  #define a função do lançamento oblíquo
  funcao=altura_inicial+(math.tan(math.radians(angulo_lancamento))+(gravidade/(coeficiente_arrasto*velocidade_inicial*math.cos(math.radians(angulo_lancamento)))))*valor_inicial+gravidade*math.log(1-(coeficiente_arrasto*valor_inicial/(velocidade_inicial*math.cos(math.radians(angulo_lancamento)))))/coeficiente_arrasto**2
  #deriva a função, aplicando o método de newton
  derivada=(math.tan(math.radians(angulo_lancamento))+gravidade/(coeficiente_arrasto*velocidade_inicial*math.cos(math.radians(coeficiente_arrasto))))-gravidade/(coeficiente_arrasto*(velocidade_inicial*math.cos(math.radians(angulo_lancamento))-coeficiente_arrasto*valor_inicial))
  #atualiza o 'valor_inicial', de modo que ele se torne cada vez mais perto da aproximação real
  valor_inicial=valor_inicial-(funcao/derivada)
  #imprime o resultado de cada iteração, indicando o número da iteração
  print("Iteração número",i,"alcance =",valor_inicial,"m")
'''
TESTE 01:
angulo_lancamento=34.5
velocidade_inicial=123.4
gravidade=9.78
altura_inicial=2.45
coeficiente_arrasto=0.03
valor_inicial=1124
'''