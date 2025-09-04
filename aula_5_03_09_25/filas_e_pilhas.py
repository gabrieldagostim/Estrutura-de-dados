

class FilaCircular():
    
    def __init__(self, capacidade):
        self.inicio = 0
        self.final = -1
        self.elementos = 0
        self.capacidade = capacidade
        self.valores = [None] * capacidade
        
    
    def fila_cheia(self):
        return self.elementos == self.capacidade
    
    
    def enfileirar(self, valor):
        if self.fila_cheia():
            print('Erro de fila cheia.')
            return
    
        if self.final == (self.capacidade - 1):
            self.final = -1

        self.final += 1
        
        self.valores[self.final] = valor
        self.elementos += 1
        
        
    def fila_vazia(self):
        return self.elementos == 0
    
    
    def desenfileirar(self):
        if self.fila_vazia():
            print('Erro de fila vazia.')
            return
        
        temp = self.valores[self.inicio]
        self.inicio += 1
        
        if self.inicio == self.capacidade:
            self.inicio = 0
        
        self.elementos -= 1
        
        return temp
    
      
    def primeiro(self):
        if self.fila_vazia():
            return -1
        return self.valores[self.inicio]


    def mostrar(self):
        print(self.valores)


fila_sus = FilaCircular(capacidade=7)

# fila_sus.enfileirar(1)
# fila_sus.mostrar()
# fila_sus.enfileirar(6)
# fila_sus.mostrar()
# fila_sus.enfileirar(8)
# fila_sus.enfileirar(5)
# fila_sus.mostrar()


# 1. Implementar em linguagem Python o pseudocódigo do algoritmo “Fila” visto em aula
# com capacidade igual a quantidade de caracteres que compõem seu primeiro nome. Faça
# também:

# a. Teste o método “filaVazia()” através do método “desenfileirar()”;
# fila_sus.desenfileirar()


# b. Demonstrar o enfileiramento de cada um dos caracteres que compõem seu
# primeiro nome;

fila_sus.enfileirar('G')
fila_sus.enfileirar('A')
fila_sus.enfileirar('B')
fila_sus.enfileirar('R')
fila_sus.enfileirar('I')
fila_sus.enfileirar('E')
fila_sus.enfileirar('L')

# c. Teste o método “filaCheia()” através do método “enfileirar(valor)”;

# fila_sus.enfileirar('lindo')

# d. Após executar as operações anteriores, demonstrar qual elemento é o primeiro
# da fila;
# print(f"O primeiro item da fila é: {fila_sus.primeiro()}")

# e. Execute o método “desenfileirar()” por três vezes e verifique qual elemento é o
# primeiro da fila.

fila_sus.desenfileirar()
fila_sus.desenfileirar()
fila_sus.desenfileirar()
# print(f'Agora o primeiro item da fila {fila_sus.primeiro()}')

# 2. O problema de inserir (enfileirar) elementos em uma Fila envolve? Explique o que
# “precisa ser feito” para inserir um elemento e quais cuidados devem ser protegidos no
# algoritmo.

# 3. O problema de retirar (desenfileirar) elementos em uma fila envolve? Explique o que
# “precisa ser feito” para retirar um elemento e quais cuidados devem ser protegidos no
# algoritmo.


# 4. Qual critério é utilizado para saber se uma Fila está vazia?
#  quando a qtd de elementos é igual a 0

# 5. Qual critério é utilizado para saber se uma Fila está cheia?
#  quando a qtd de elementos é igual a capacidade

# 6. Considere a Fila:
# S A
# a. Insira a sequência T,C na Fila e demonstre esse procedimento através do
# preenchimento da tabela abaixo:
# final elementos

# +---+----------+------------+
# | final    |  elementos    |
# +---+----------+------------+
# |    0    |      3         |
# |    1    |      4         |
# |         |                |
# |         |                |
# +---+----------+------------+


# b. Qual o valor do atributo “final” após a inserção da sequência descrita no item
# o valor final vai para 1

# c. Se você fosse “desenfileirar” um elemento da Fila, qual seria esse elemento?
# elemento S

# d. Desenfileirar dois elementos da fila e demonstrar esse procedimento através
# da tabela abaixo:

# +---+----------+------------+
# | início   |   elementos    |
# +---+----------+------------+
# |    3    |       3         |
# |    0    |       2         |
# |         |                 |
# |         |                 |
# +---+----------+------------+


class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1 
        self.valores = [None] * self.capacidade    


    def empilhar(self, valor):
        if(self.pilha_cheia()):
            print("Pilha cheia!")
        else:            
            self.topo = self.topo + 1
        self.valores[self.topo] = valor    
        
        
    def pilha_cheia(self):
        return self.topo == self.capacidade -1
    
    
    def pilha_vazia(self):
        return self.topo ==  -1
    
    
    def ver_topo(self):
        if(self.topo != -1):
            return self.valores[self.topo]
        else:
            return -1    
        
        
    def desempilhar(self):
        if(self.pilha_vazia()):
            print("Pilha vazia!")
        else:
            self.topo = self.topo -1


pilha = Pilha(capacidade=4)
# A)



# 7. Implementar em linguagem Python o pseudocódigo do algoritmo “Pilha” visto em
# aula. Faça também:


# a. Teste o método pilha_cheia()” através do método “desempilhar()”;
pilha.desempilhar()


# b. Demonstrar o empilhamento de cada um dos caracteres que compõem seu
# primeiro nome;

pilha.empilhar('G')
pilha.empilhar('A')
pilha.empilhar('B')
pilha.empilhar('R')
pilha.empilhar('I')
pilha.empilhar('E')
pilha.empilhar('L')

# c. Teste o método “pilhaCheia()” através do método “empilhar(valor)”;

# R: 
# pilha.empilhar("A")

# d. Após executar as operações anteriores, demonstrar qual elemento está no
# topo da Pilha
print(pilha.ver_topo())

# e. Execute o método “desempilhar()” por três vezes e verifique qual elemento
# está no topo da Pilha;

pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()

# 8. Suponha que você insira a sequência “S, A, T, C” em uma Pilha. Então você
# desempilha três elementos. Qual o valor do atributo topo da Pilha?

# O valor seria C pois foi o último a ser inserido

# 9. Qual o principal problema envolvido no algoritmo que implementa a Pilha?

#  Eu sou vou poder acessar o primeiro item que foi adicionado assim que eu remover os outros que foram add depois dele

# 10. Qual critério é utilizado para saber se uma Pilha está vazia?

# se o topop é = -1


# 11. Qual critério é utilizado para saber se uma Pilha está cheia? 

# se o topo for igual a capacidade -1