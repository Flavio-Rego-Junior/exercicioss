#Crie uma função chamada saudacao_personalizada que aceite um parâmetro chamado nome.
#A função deve imprimir uma mensagem de boas-vindas que inclua o nome fornecido, como "Olá, [nome]! Tenha um ótimo dia.".
#Chame a função duas vezes, com nomes diferentes como argumentos.
def saudação_personalizada (nome):
   saudação =  print("olá ",nome, "tenha um otimo dia")
   return saudação
lista_de_nomes = []
for i in range(2):
   print("pfv digite um nome")
   nome = input(">>>")
   saudação_personalizada(nome)
 