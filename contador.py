import re
"""Armazenando o texto do usuário"""
arquivo_texto = open('texto.txt', 'w', encoding='UTF-8')
texto_usuario = input("Digite ou cole aqui o seu texto: ")
arquivo_texto.write(texto_usuario)
arquivo_texto.close()

"""Tansformando o texto em uma string sem separadores, exceto espaço"""
with open('texto.txt', 'r', encoding='UTF-8') as texto:
    lista_palavras_texto = [[str(word) for word in line.split()] for line in texto.readlines()]

lista = []

for wrd in lista_palavras_texto:
    i = 0
    while i < len(wrd):
        lista.append(wrd[i].upper())
        i += 1

novo_texto = ' '.join(lista)

"""Buscando a palavra desejada pelo usuário"""
palavra = input("Qual palavra deseja saber a ocorrência?: ")
lista_total_palavra = re.findall(palavra, novo_texto, flags=re.I)
total_palavra = len(lista_total_palavra)

"""Imprimindo o total de ocorrências da palavra digitada pelo usuário"""
print(f'O total de ocorrências da palavra {palavra} é: {total_palavra}')
