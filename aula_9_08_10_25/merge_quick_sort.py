import random


def merge_sort(lista: list) -> list:
    
    # divisão do array
    if len(lista) > 1:
        divisao = int(len(lista) // 2)
        esquerda = lista[0:divisao]
        direita = lista[divisao:]
        
        merge_sort(esquerda)
        merge_sort(direita)
        
        i = j = k = 0
        
        # Ordena esquerda e direita
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[i]
                j += 1
            k += 1
            
        # Ordenação final
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1
        
        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1
            
        return lista


## Quick Sort
def particao(lista:list, inicio: int, final:int) -> list:
    pivo = lista[final]
    i = inicio - 1
    
    for j in range(inicio, final):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j], = lista[j], lista[i]
    lista[i + 1], lista[final] = lista[final], lista[i + 1]
    return i + 1
        

def quick_sort(lista:list, inicio, final):
    if inicio < final:
        posicao = particao(lista, inicio, final)
        
        # esquerda
        quick_sort(lista, inicio, posicao - 1)
        
        # direita
        quick_sort(lista, posicao + 1, final)
        
        return lista
    
lista_aleatoria = [random.randint(1, 1000) for _ in range(1000)]

# 1. Implementar em linguagem Python o pseudocódigo do algoritmo “Merge Sort”
# visto na Aula. Faça também:
# a. Demonstrar a ordenação de uma lista de 1000 números;
lista_mil = [random.randint(1, 1000) for _ in range(1000)]
lista_ord = merge_sort(lista=lista_mil)


# b. Demonstre a ordenação da lista de nomes fornecida.
# print(lista_ord)


# 2. Implementar em linguagem Python o pseudocódigo do algoritmo “Quick Sort”
# visto na Aula. Faça também:

# a. Demonstrar a ordenação de uma lista de 1000 números;
ordenada = quick_sort(lista_aleatoria, 0, len(lista_aleatoria) - 1)

# b. Demonstre a ordenação da lista de nomes fornecida.
# print(ordenada)

# 3. Dado o array [8, 6, 4, 2, 0], uma chamada de ordenação através do algoritimo
# Quick Sort, cujo a assinatura da função é quick_sort(array, inicio, final) é feita de
# qual forma?

#>>> d. quick_sort( array, 0, len(array) – 1);