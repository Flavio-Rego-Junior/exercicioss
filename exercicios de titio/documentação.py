#Pegue a função filtrar_pares do exercício 7.
#Adicione a ela uma docstring de múltiplas linhas completa, seguindo as convenções da PEP 257. A docstring deve incluir:
#Uma linha de resumo no modo imperativo.
#Uma descrição mais detalhada do que a função faz.
#Uma seção Args: para descrever o parâmetro.
#Uma seção Returns: para descrever o valor de retorno.

#Dica Final: Para cada exercício, pense primeiro nos "canais de comunicação" da sua função:
#O que ela precisa receber? (Seus parâmetros)
#O que ela precisa devolver? (Seu valor de return)
lista_de_numeros = []
"""retorne uma parametro para ser utilizado no filtro."""
def apenas_pares (x): 
    return x % 2 == 0 
"""a função emite um parametro que é que usei para tirar qualquer um que nao se encaixa nele """

while True:
    print("você deseja adicionar algum numero a lista ? (sim/nao)")
    continuar = input(">>> ")
    if continuar == "nao":
        break

    print("digite o numero que deseja adicionar")
    numero_adicionar = int(input(">>> "))
    lista_de_numeros.append(numero_adicionar)


"""filtre a lita"""
paresF = filter(apenas_pares, )
print((list(paresF)))
"""return: a def em si so retornou um parametro, mas aqui esta printando todos os valores pares dela pares"""