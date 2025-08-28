class VetorOrdenado():
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = [None] * capacidade
        
        
    def inserir(self, valor):
        
        if self.ultima_posicao == self.capacidade -1:
            print('Vetor Cheio')
            return

        posicao = 0 
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x = x - 1
            
        self.valores[posicao] = valor
        self.ultima_posicao += 1                    
   
            
    def mostrar(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio.')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i,'-',self.valores[i])


    def pesquisa_linear(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                return -1
            
            if self.valores[i] == valor:
                return i
            
            if i == self.ultima_posicao:
                return -1

    
    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao
        
        while True:
            posicao_atual = (limite_inferior + limite_superior) // 2
            
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            
            elif limite_inferior > limite_superior:
                return -1

            else:
                # divide novamente para encontrarr
                
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                    
                else:
                    limite_superior = posicao_atual - 1
        
    def excluir(self, valor):
        posicao = self.pesquisa_binaria(valor)
        if posicao == -1:
            return -1
        
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1
        
        
        
vet = VetorOrdenado(7)

# a. Demonstrar a inserção de cada um dos caracteres que compõem seu primeiro nome;

vet.inserir('G')
vet.inserir('A')
vet.inserir('B')
vet.inserir('R')
vet.inserir('I')
vet.inserir('E')
vet.inserir('L')


# b. Demonstrar a impressão do vetor criado;
vet.mostrar()

# c. Demonstrar a pesquisa por pelo menos três caracteres existentes no vetor;

print('....pesquisando letras')
print(vet.pesquisa_binaria('A'))


print('....pesquisando letras')
print(vet.pesquisa_binaria('R'))


print('....pesquisando letras')
print(vet.pesquisa_binaria('E'))


# d. Demonstrar a exclusão de caracteres do início, meio e final do vetor;

vet.excluir('G')
vet.excluir('L')
vet.excluir('B')

# e. Demonstrar a impressão do vetor após as remoções.

vet.mostrar()


# 2. Considere um vetor ordenado com capacidade igual a 7 elementos contendo em seu interior
# a sequência “2, 3, 5, 7”. Responda:

# [2][3][4][5][7][][]
#  0  1  2  3  4

# a. Após a inserção da sequência, qual o valor do atributo “ultima_posiçao”?
# R: 3

# b. Se inserirmos o elemento cujo valor é igual a 4, quantas iterações serão necessárias
# para realocar os demais elementos do vetor?
# R: e

# c. Qual o novo valor do atributo “ultima_posiçao”?
# R: 4

# d. Com base no algoritmo de pesquisa linear, quantas iterações serão necessárias para
# encontrar o índice do vetor que contém o valor 7?
# R: 5 interações

# e. Com base no algoritmo de pesquisa binária, quantas iterações serão necessárias para
# encontrar o índice do vetor que contém o valor 7?
#  R: 3 interações


# 3. Considere um vetor ordenado com capacidade igual a 7 elementos contendo em seu interior
# a sequência “A,C,D,F”:

# [A][C][D][F][ ][ ][ ]
#  0  1  2  3  4  5  6 

# a. Faça o desenho do vetor contendo o tamanho e a sequência descrita no enunciado;
# R:

'''
b. Preencha os campos das tabelas abaixo para a inserção do valor B.


c. Refaça o desenho do vetor após a remoção do elemento descrito no ítem b)

#  Buscar posição
| i  | posição | valores[i] |
|----|---------|------------|
| 0  |    0    |     A      |
| 1  |    1    |     C      |
|    |         |            |
|    |         |            |


#  Realocar valores
| posição | x | valores[x] |
|---------|---|------------|
|    1    | 4 |    F       |
|    1    | 3 |    D       |
|    1    | 2 |    C       |
|    1    | 1 |    B       |
|    1    | 0 |            |
Finaliza
'''