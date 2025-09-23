#Crie uma função palavra_mais_longa que receba uma frase (string) como parâmetro.
#A função deve retornar a palavra mais longa da frase. Se houver empate, pode retornar qualquer uma das palavras mais longas.

#Dica: O método .split() pode ser útil para transformar a frase em uma lista de palavras.
#Dica Final: Para cada exercício, pense primeiro nos "canais de comunicação" da sua função:
#O que ela precisa receber? (Seus parâmetros)
#O que ela precisa devolver? (Seu valor de return)

def palavra_mais_longa (x):
   x = str(x)
   lista_de_palavras = x.split()
   numero_de_vezes = len(lista_de_palavras)
   maior_palavra = (" ")
   for i in range(numero_de_vezes):
        if len(lista_de_palavras[i]) > len(maior_palavra):
          maior_palavra = lista_de_palavras[i]
   return maior_palavra
print("escreva uma frase")
frase = input(">>> ")
frase_limpa = frase.strip()
maior = palavra_mais_longa(frase)
print("a maior palavra foi :", maior)



    
    