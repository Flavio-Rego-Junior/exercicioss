#Dada a lista numeros = [1, 2, 3, 4, 5].
#Use a função map() junto com uma função lambda para criar uma nova 
# lista que contenha o quadrado de cada número da lista original.

#Dica Final: Para cada exercício, pense primeiro nos "canais de comunicação" da sua função:
#O que ela precisa receber? (Seus parâmetros)
#O que ela precisa devolver? (Seu valor de return)
lista_de_numeros = []

while True:
    print("adicione um numero")
    adicionar_numero = int(input(">>> "))
    lista_de_numeros.append(adicionar_numero)
    print("você deseja continuar adiconando numeros(sim/nao)")
    contiuar = input(">>> ")
    if contiuar == "nao":
        break
Numeros_ao_quadrado = list(map(lambda x: x**2, lista_de_numeros))
print(Numeros_ao_quadrado)