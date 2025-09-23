#Escreva uma função chamada eh_maior_de_idade que receba uma idade como parâmetro.
#A função deve retornar True se a idade for 18 ou mais, e False caso contrário.
#Teste a função com diferentes idades.

#Dica Final: Para cada exercício, pense primeiro nos "canais de comunicação" da sua função:
#O que ela precisa receber? (Seus parâmetros)
#O que ela precisa devolver? (Seu valor de return)
def eh_maior_de_idade (idade):
    if idade >= 18:
     maior_idade = True
    else:
       maior_idade = False
    return maior_idade
print("digite sua idade")
idade_digitar = int(input(">>> "))
maior_idade_F = eh_maior_de_idade(idade_digitar)
print(maior_idade_F)