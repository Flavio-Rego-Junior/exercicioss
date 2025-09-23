#Crie uma função chamada operacoes_basicas que receba dois números, a e b, como parâmetros.
#A função deve retornar quatro valores: a soma, a subtração, a multiplicação e a divisão de a por b.
#Chame a função e desempacote os resultados em quatro variáveis distintas. Imprima cada resultado.

#Desafio: Como você pode garantir que a função não cause um erro se b for igual a zero?
#Dica Final: Para cada exercício, pense primeiro nos "canais de comunicação" da sua função:
#O que ela precisa receber? (Seus parâmetros)
#O que ela precisa devolver? (Seu valor de return)
def operações_basicas (a, b):
    soma = a + b
    subtraçao = a - b
    multiplicao = a*b
    if a and b != 0:
      divisao = a/b
    else:
     divisao = ("não é possivel dividir por 0")
    operações = [soma, subtraçao, multiplicao, divisao]
    return operações
print("Vamos fazer todas operções basicas")
print("escolha seu primeiro numero")
numero1 = int(input(">>> "))
print("escolha seu segundo numero")
numero2 = int(input(">>>"))

operações_lista = operações_basicas(numero1, numero2)
somaF = operações_lista[0]
subtraçaoF = operações_lista[1]
multiplicacao = operações_lista[2]
divisao = operações_lista[3]
print("a soma é =", somaF )
print("a subtração =", subtraçaoF)
print("a multiplicacao é =", multiplicacao)
print("a divisão é =", divisao)