#Escreva uma função filtrar_pares que receba uma lista de números.
#A função deve retornar uma nova lista contendo apenas os números pares da lista original.

#Exemplo: filtrar_pares([1, 2, 3, 4, 5, 6]) deve retornar [2, 4, 6].

#Dica Final: Para cada exercício, pense primeiro nos "canais de comunicação" da sua função:
#O que ela precisa receber? (Seus parâmetros)
#O que ela precisa devolver? (Seu valor de return)
lista_de_numeros = []

def parametro (l):
    return l % 2 == 0 
def apenas_pares (x): 
    pares = filter(parametro, x)
    paresF = list(pares)
    return paresF

while True:
    print("você deseja adicionar algum numero a lista ? (sim/nao)")
    continuar = input(">>> ")
    if continuar == "nao":
        break
    print("digite o numero que deseja adicionar")
    numero_adicionar = int(input(">>> "))
    lista_de_numeros.append(numero_adicionar)
pares_saida = apenas_pares(lista_de_numeros)
print(pares_saida)



