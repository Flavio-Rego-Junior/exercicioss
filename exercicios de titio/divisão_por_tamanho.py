#Estes exercícios introduzem o uso de funções lambda para tarefas concisas.

#Você tem a seguinte lista: nomes =.
#Use a função sorted() com uma função lambda como chave (key) 
#para ordenar a lista de nomes pelo número de caracteres, do menor para o maior.

#Dica Final: Para cada exercício, pense primeiro nos "canais de comunicação" da sua função:
#O que ela precisa receber? (Seus parâmetros)
#O que ela precisa devolver? (Seu valor de return)
lista_de_nomes = []
while True:
    print("adicione um nome")
    adicionar_nome = str(input(">>> "))
    lista_de_nomes.append(adicionar_nome)
    print("você deseja continuar adiconando nomes ?(sim/nao)")
    contiuar = input(">>> ")
    if contiuar == "nao":
        break
lista_ordenada = sorted(lista_de_nomes, key= lambda tamanho: -(len(tamanho)))
print(lista_ordenada)
    
