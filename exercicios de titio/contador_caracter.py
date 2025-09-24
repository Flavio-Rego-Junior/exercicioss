#Crie uma função contar_caracteres que aceite uma string como argumento.
#A função deve retornar o número de caracteres na string, sem contar os espaços em branco no início e no fim.

#Dica: Pesquise sobre o método .strip() para strings.
#Dica Final: Para cada exercício, pense primeiro nos "canais de comunicação" da sua função:
#O que ela precisa receber? (Seus parâmetros)
#O que ela precisa devolver? (Seu valor de return
def contar_caracteres (x):
    palavra_suja = str(x)
    palavra_limpa = palavra_suja.strip()
    numero_caracter = len(palavra_limpa)
    return numero_caracter
print("escreva uma oalavra")
palavra = str(input(">>>"))
contagemF =  contar_caracteres(palavra)
print("essa palvra tem",contagemF, "caracteres, não contando os espaços de inicio e fim ")

