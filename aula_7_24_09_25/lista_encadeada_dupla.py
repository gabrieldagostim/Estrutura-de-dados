
class No():

    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

    def mostra_no(self):
        print(f'[{self.valor}]')
        
        
class ListaDuplamenteEncadada():
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        
        
    def lista_vazia(self):
        return self.primeiro == None  


    def pesquisar_valor(self, valor):
        if self.primeiro is None:
            print('Erro de lista vazia')
            return None

        atual = self.primeiro

        while atual is not None:
            if atual.valor == valor:
                return atual
            atual = atual.proximo

        return None

    def inserir_inicio(self, valor):
        novo = No(valor)
        if self.lista_vazia():
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo
        novo.proximo = self.primeiro
        self.primeiro = novo


    def inserir_final(self, valor):
        novo = No(valor)
        if self.lista_vazia():
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo
            
        self.novo.proximo = self.primeiro 
        self.primeiro = novo
    
    
    def mostrar_inicio(self):
        atual = self.primeiro
        
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo
    
    
    def mostrar_final(self):
        atual = self.ultimo
        
        while atual != None:
            atual.mostra_no()
            atual = atual.anterior
    
    
    def excluir_inicio(self):
        temp = self.primeiro
        if self.primeiro == None:
            self.ultimo = None
            
        else: 
            self.primeiro.proximo.anterior = None
        self.primeiro = self.primeiro.proximo
        
        return temp
    
    
    def excluir_final(self):
        temp = self.ultimo
        if self.primeiro.proximo == None:
            self.primeiro = None
            
        else:
            self.ultimo.anterior.proximo == None
        self.ultimo = self.ultimo.anterior
        
        return temp

        
    
    def excluir_posicao(self, valor):
        atual = self.primeiro
        
        while atual.valor != valor:
            atual = atual.proximo
            if atual == None:
                return None
            
        if atual == self.primeiro:
            self.primeiro = atual.proximo
        else:
            atual.anterior.proximo = atual.proximo
        
        if atual == self.ultimo:
            self.ultimo = atual.anterior
        else:
            atual.proximo.anterior = atual.anterior
        
        return atual
        
    
    

if __name__ == '__main__':
    
    
    
    # lista = ListaDuplamenteEncadada()
    
    # lista.inserir_inicio(5)
    # lista.inserir_inicio(2)
    # lista.inserir_inicio(5)
    # lista.inserir_inicio(8)
    # lista.mostrar_final()
    
# ___ EXERCICIO ___


# 1. Implementar em linguagem Python o pseudocódigo do algoritmo “Lista
# Encadeada Dupla” visto em aula. Faça também:

# a. Demonstrar a inserção de cada um dos caracteres que compõem seu
# primeiro nome;

    lista = ListaDuplamenteEncadada()
    
    lista.inserir_inicio('G')
    lista.inserir_inicio('A')
    lista.inserir_inicio('B')
    lista.inserir_inicio('R')
    lista.inserir_inicio('I')
    lista.inserir_inicio('E')
    lista.inserir_inicio('L')

    
# b. Demonstre a impressão de todos os elementos inseridos no item a;

    # lista.mostrar_final()
    # print()


# c. Faça a exclusão do primeiro elemento da lista;

    # lista.excluir_inicio()
    
# d. Verifique se a operação executada no item c foi concluída;

    # lista.mostrar_inicio()
    # print()
    
# e. Faça a pesquisa pelo último caractere do seu nome. Qual o retorno do
# algoritmo?

    # retorno = lista.pesquisar_valor('G')
    # retorno.mostra_no()
    # lista.mostrar_final()
    

# f. Escolha um elemento qualquer (não pode ser o primeiro) e faça a sua
# exclusão.

    # lista.excluir_posicao('A')

# g. Verifique se a operação executada no item f foi concluída;

    # lista.mostrar_final()


# 2. Considere uma Lista Encadeada Dupla vazia. Insira no início da lista a sequência
# de valores 3, 7 e 6. Demonstre de forma detalhada (desenho) a inserção dos nós
# e a inserção e sobrescrita dos ponteiros.


l2 = ListaDuplamenteEncadada()
l2.inserir_inicio(3)
l2.inserir_inicio(7)
l2.inserir_inicio(6)


# 3. Faça a exclusão do elemento 7 da lista preenchida na Questão 2. Demonstre
# através de desenho os detalhes da exclusão do elemento solicitado bem como a
# sobrescrita dos ponteiros.

l2.excluir_posicao(7)
l2.mostrar_final()

# 4. Onde pode ser realizada a inserção de novos elementos em uma Lista Encadeada
# Dupla?

# R: No inicio da lista

# 5. Qual o nome da estrutura que a Lista Encadeada Dupla utiliza para guardar seus
# dados?

# R: nó

# 6. Qual critério é utilizado para saber se uma Lista Encadeada Dupla está vazia?

# Se a cabeça da lista aponta para null/terra

# 7. Qual critério é utilizado para saber se o algoritmo de busca está no último
# elemento de uma Lista Encadeada Dupla?

# Proximo é none/terra