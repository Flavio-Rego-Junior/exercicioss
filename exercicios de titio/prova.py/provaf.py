
#tentando colocar o negocio dos arquivos
#○ Cada tarefa será um dicionário (ex: {'descricao': 'Estudar 
#Python', 'concluida': False}). lista_inicial = []
lista_inicial2 = []
lista_pricipal = []
listas = []
contador = 0
contador2 = 0


arquivo = open('lista_de_tarefas.txt','w') 
open('lista_de_tarefas.txt', 'r')
for i in 'lista_de_tarefas.txt':
     lista_pricipal.append(i)

"""criando lista"""
def criar_listas (x):
     
     print("escreva uma descrição para sua lista")
     descrição= input(">>> ")
     comclusão = "ainda não foi feita"
     lista = {'id':contador,'descrição': descrição,"comclusao": comclusão  }
     lista_pricipal.append(lista)
     return lista
"""adicionando a parte de comclusão"""

"""listar tarefas"""
def listando_os_dicionarios (x):
   for i in range(len(lista_pricipal)):
    x =  print(lista_pricipal[i]['id'], lista_pricipal[i]['descrição'])
   return x


      
"""atualizando as listas"""
def atualizando_listas (l):
    print("oque vc deseja atualizar na lista ?(1 para descriçao/2 para comclusão)")
    oque_deseja_atualizar = (input(">>> "))
    if oque_deseja_atualizar == "1":
       print("digite o id da tarefa q vc deseja atualizar a descrição")
       numero = int(input(">>> "))
       print("digite oque vc deseja colocar na descrição")
       atualizando_desc = input(">>> ")
       lista_pricipal[numero - 1]["descrição"] = atualizando_desc

    elif oque_deseja_atualizar == "2":
     print("digite o id da tarefa q vc deseja atualizar a comclusão")
     numero = int(input(">>> "))
     lista_pricipal[numero - 1]["comclusao"] = "feita"
     
     return numero
    



def remover_tarefa (x):
   print("digite o id da tarefa que vc deseja remover")
   numero_escrever = int(input(">>> "))
   numero_para_retirada = (numero_escrever - 1)
   del lista_pricipal[numero_para_retirada]
   return numero_escrever
   


while True:
   print("oque vc deseja fazer ?")
   print("opções ↓↓↓(digete o numero correspondente a oque vc quer fazer)")
   print("criar uma tarefa(1), listar tarefas(2), atualizar uma tarefa(3), remover uma tarefa(4), não desejo fazer nada(5)")
   escolha_do_usario = input(">>> ")
   if escolha_do_usario == "1":
    contador += 1
    lista_de_negociola = [criar_listas(contador)]
   elif escolha_do_usario == "2":
      x = listando_os_dicionarios(1)
      print(x)
   elif escolha_do_usario == "3":
      atualizando_listas(1)
   elif escolha_do_usario == "4":
      remover_tarefa(1)
   elif escolha_do_usario == "5":
      break
   else:
      print("oque vc digitou não é compativel com nenhuma das opções existentes, tente novamente")
print(lista_pricipal)

for i in lista_pricipal:
    arquivo.write(i)
arquivo.close()
 