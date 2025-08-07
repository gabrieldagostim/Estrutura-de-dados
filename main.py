
# 1 variáveis em python
# 
nome = 'gabriel' # str
altura = 1.95 # float
idade = 26  # int
ativo = True # bool

print(nome, idade, altura, ativo)


# 2 Estrutura condicional
if idade > 18 or nome.startswith('er'):
    print('Ou seu nome começa com "er" ou tem mais de 18 anos...')


if idade > 18 and idade <= 40:
    print(f'Maior de idade')

elif idade > 40:
    print(f'Você está velho.')

else:
    print('menor')


for i in range(0, 10 -1):
    print(i)

contador = 0
while contador < 5:
    print(f'Contador: {contador}')

    contador += 1


# 4: Listas

frutas = ['maçã', 'banana']

frutas.append('uva')
frutas.remove('maçã')

# 5 Dicionários

aluno = {
    "nome": "Joao",
    "idade": 20,
    "nota":  8.5,
}

print(aluno['nome'])

# 6 Tuplas

ah = ()
gabriel_tupla = 5,6
print(type(gabriel_tupla))


# 7 Funções 
def saudacao(nome):
    return f'Olá, {nome}'

def imprime_saudacao(msgsaudacao):
    print(msgsaudacao)

print(imprime_saudacao('aula de programação'))


