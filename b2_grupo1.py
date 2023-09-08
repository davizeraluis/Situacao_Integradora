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
#Bibliotecas
import math

#Funçoes
#Função que converte graus em radianos
def convercao_graus_rad(angulo_graus):
    angulo_rad=math.radians(angulo_graus)
    return angulo_rad
#Função que calcula o limite por definição
#Método de Newton
#def metodo_newton(palpite,iteracoes):
    

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
x=float(0)
#Resultado final
resultado_final=float(0)

#Processamento
angulo_lancamento=convercao_graus_rad(angulo_lancamento)
#Chamar a função metodo de newton

#Fórmula do lançamento oblíquo
for i in range(0,numero_iteracoes):
    resultado_final=float(altura_inicial+(math.tan(angulo_lancamento)+(gravidade/(coeficiente_arrasto*velocidade_inicial*math.cos(angulo_lancamento))))*x+(gravidade/coeficiente_arrasto**2)*math.log(1-coeficiente_arrasto/(velocidade_inicial*math.cos(angulo_lancamento))*x))
    print(resultado_final)