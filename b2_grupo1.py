'''
Algoritmo calculo_lancamento_obliquo_por_metodo_de_newton
Situação Integradora EsPCEx 11/08/2023
Turma B2 - Grupo 1
6153 Barreto
7035 Zefiro
7230 Rezende Silva
7245 Rocha Oliveira
7335 Pasquali
7804 Maria Júlia
7832 Vitória Gomes
'''
#Entrada de Dados
#Entrada dos parâmetros da função
angulo_lancamento=float(input("Digite o ângulo de lançamento (em graus): "))
velocidade_inicial=float(input("Digite a velocidade incial: "))
gravidade=float(input("Digite o valor da gravidade: "))
altura_inicial=float(input("Digite a altura inicial do lançamento: "))
coeficiente_arrasto=float(input("Digite o coeficiente de arrasto: "))

#Entrada do parâmetros do método de newton
valor_inicial=float(input("Digite um valor inicial aproximado para o alcance: "))
numero_iteracoes=float(input("Digite o número de iterações desejada: "))
resultado=float(0)

#Constantes
EULER=float(2,718281)