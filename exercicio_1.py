# 1. Crie uma função que recebe uma lista de números inteiros e retorna uma nova lista contendo apenas os 
# números pares.

lista_numeros = [1, 2, 3, 4, 5, 6]

def retorna_pares(lista_nums):
    nums_pares = []
    try:
        for num in lista_nums:
            if num % 2 == 0:
                nums_pares.append(num)

        return nums_pares
    except Exception as e:
        return None
    
# lista_pares = retorna_pares(lista_numeros)
# print(lista_pares)


# 2. Crie uma função que recebe uma string e retorna um dicionário com a contagem de cada caractere 
# presente na string.


def cria_dici(txt):
    dici = {}

    def conta_caractere(caract, txt):
        qtd = 0
        for letra in txt:
            if letra == caract:
                qtd += 1
        return qtd

    for caract in txt:
        dici[caract] = conta_caractere(caract=caract,txt=txt)
    return dici

# a = cria_dici('keko')
# print(a)


# 3. Crie uma função que recebe um dicionário onde as chaves são nomes de alunos e os valores são listas 
# com suas notas. A função deve calcular a média das notas de cada aluno e retornar um novo dicionário 
# com os nomes e suas respectivas médias.

alunos_dict = {
    'gabriel': [10,8,9],
    'eric': [2,3,1]
}

def calcula_media(alunos_dict):
    medias_alunos = {}
    
    for aluno in alunos_dict:
        media = sum(alunos_dict[aluno]) / len(alunos_dict[aluno])
        medias_alunos[aluno] = media
    return medias_alunos

# medias = calcula_media(alunos_dict=alunos_dict)
# print(medias)


# 4. Crie uma função que recebe uma lista vazia e permite ao usuário adicionar 5 elementos a essa lista. Ao 
# final, a função deve retornar a lista completa.

lista_vazia = []
lista_preenchida = []

def add_elemento(lista_vazia):

    for i in range(5):
        elemento = input(f'Insira o elemento {i}/5')
        lista_preenchida.append(elemento)
    
    return lista_preenchida

# lista_preenchida = add_elemento(lista_vazia)
# print(lista_preenchida)


# 5. Escreva uma função que recebe uma lista de números inteiros e retorna a soma de todos os elementos 
# da lista

lista_numeros_inteiros = [1,5,4,6,8,1,10]

def soma_nums_lista(lista):
    return sum(lista)

soma = soma_nums_lista(lista_numeros_inteiros)
print(soma)


