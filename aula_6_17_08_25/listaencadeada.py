

class No():
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo
    
    def imprime(self):
        print(f'[{self.valor}]')


class ListaEncadeada():
    
    def __init__(self, primeiro=None):
        self.primeiro = primeiro

    
    def inserir_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo


    def mostrar(self):
        if self.primeiro == None:
            print('Erro na lista vazia.')
            return None
        
        atual = self.primeiro
        
        while atual != None:
            atual.imprime()
            atual = atual.proximo
            
    
    
    def pesquisar(self, valor):
        if self.primeiro == None:
            print('Erro de lista vazia.')
            return None
        atual = self.primeiro
        while atual.valor != valor:
            if atual.proximo ==  None:
                return None
            else:
                atual = atual.proximo
        return atual
                
        
    
    def excluir_inicio(self):
        if self.primeiro == None:
            print('Erro de lista vazia')
            return None
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp
    
    
    
    def exlcuir_posicao(self, valor):
        if self.primeiro == None:
            print('Erro de lista vazia')
            return None
        atual = self.primeiro
        anterior = self.primeiro
        
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                anterior = atual
                atual = atual.proximo
        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo
        return atual
    
# EXERCICIOS
 # 1 A
# Demonstrar a inserção de cada um dos caracteres que compõem seu
# primeiro nome;

print('Demonstrar a inserção de cada um dos caracteres que compõem seu primeiro nome;')

lista_encadeada = ListaEncadeada()

lista_encadeada.inserir_inicio('g')
lista_encadeada.inserir_inicio('a')
lista_encadeada.inserir_inicio('b')
lista_encadeada.inserir_inicio('r')
lista_encadeada.inserir_inicio('i')
lista_encadeada.inserir_inicio('e')
lista_encadeada.inserir_inicio('l')
print()

# b. Demonstre a impressão de todos os elementos inseridos no item a;
print('b. Demonstre a impressão de todos os elementos inseridos no item a;')

lista_encadeada.mostrar()

# c. Faça a exclusão do primeiro elemento da lista;

print('c. Faça a exclusão do primeiro elemento da lista;')
lista_encadeada.excluir_inicio()


# d. Verifique se a operação executada no item c foi concluída;
print('d. Verifique se a operação executada no item c foi concluída;')
lista_encadeada.mostrar()

# Faça a pesquisa pelo último caractere do seu nome. Qual o retorno do
# algoritmo?

print('Faça a pesquisa pelo último caractere do seu nome. Qual o retorno do algoritmo?')

retorno = lista_encadeada.pesquisar('a')
retorno.imprime()


# f Escolha um elemento qualquer (não pode ser o primeiro) e faça a sua
# exclusão.

print('Escolha um elemento qualquer (não pode ser o primeiro) e faça a sua exclusão.')
lista_encadeada.exlcuir_posicao('a')

# g Verifique se a operação executada no item f foi concluída;
print('g Verifique se a operação executada no item f foi concluída;')
lista_encadeada.mostrar()

# Considere uma Lista Encadeada Simples vazia. Insira no início da lista a
# sequência de valores 3, 7 e 6. Demonstre de forma detalhada (desenho) a
# inserção dos nós e a inserção e sobrescrita dos ponteiros.
'''
[ cbç ] 

[ cbç ] -> [[6][->]] -> [[7][->]] -> [[3][None]]

'''

# 3. Considere uma Lista Encadeada Simples contendo a partir do seu início os
# elementos 1, 5, 3 e 2. Desenhe a lista e faça a exclusão do elemento 3 através
# do preenchimento da Tabela abaixo. Demonstre através de desenho os detalhes
# da exclusão do elemento solicitado.

'''
+-------+---------+------------+
| valor |  atual  |  anterior  |
+-------+---------+------------+
|   3   |    5    |      1     |
+-------+---------+------------+
|   3   |    3    |      5     |
+-------+---------+------------+
|   3   |    3    |      2     |
+-------+---------+------------+
'''