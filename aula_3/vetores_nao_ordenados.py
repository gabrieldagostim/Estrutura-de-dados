class Vetor():
    def __init__(self, capacidade):
        self.capacidade = capacidade # quanto cabe no meu vetor
        self.ultima_posicao = -1
        self.valores = ['[]' for i in range(capacidade)]
        
        
    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade -1:
            print('Vetor cheio')
            
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor 
        
        
    def mostrar(self):
        if self.ultima_posicao == -1:
            print('Vetor vazio')
            
    
        for i in range(self.ultima_posicao+1):
            print(i, '-', self.valores[i])
        

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i 
        return -1
    
    
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        
        if posicao == -1:
            return -1

        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1    
    

cap_teste = 5
nums_inserir = [1, 5, 9, 30, 5]
vet = Vetor(cap_teste)

for i in range(nums_inserir):
    vet.inserir(nums_inserir[i])
    
vet.mostrar()

posicao_pesquisa = vet.pesquisar(5)
print('Indice:',posicao_pesquisa)

vet.excluir(8)
vet.mostrar()