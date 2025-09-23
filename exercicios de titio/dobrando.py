#Defina uma função chamada calcular_dobro que aceite um número como parâmetro.
#A função deve calcular o dobro desse número e retornar o resultado.
#Chame a função com um número, armazene o resultado em uma variável e imprima essa variável.
def dobrar (x):
    dobrando = x*2
    return dobrando
print("escolha um numero")
escolher_numero = float(input(">>> "))
dobrado = dobrar(escolher_numero)
print("o numero dobrado", escolher_numero, "é =", dobrado)
