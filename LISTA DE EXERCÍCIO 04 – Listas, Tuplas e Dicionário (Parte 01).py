#!/usr/bin/env python
# coding: utf-8

# lista(list)

# In[ ]:


alunos = ['Amanda','Ana','Bruno','João']
notas = [10, 8.5, 7.8, 8.0]
alunos[3]# Retornar 1 elemento da lista

# Verificando o tipo de dado
print(type(alunos))
print(type(notas))

# Adicionar um novo elemento
alunos.append('Adriano')
alunos

# Remover um elemento

alunos.remove('João')
alunos


# Tuplas (tuple)

# In[ ]:


valores = (90, 79, 54, 32, 21)
pontos = (100, 94.05, 86.8, 62)





# In[ ]:


my_list = [1, 2] # Criando uma lista

my_tuple = (1, 2) # Criando uma tupla

other_tuple = (3, 4)# Criando uma tupla

my_list [1] = 3 # Substituição um elemento de uma lista


# #Tratamento de erro vai executar as ações do bloco TRY, caso não haja erro
# #Se houver um erro, ele vai executar ações do bloco Except TypeError
# try:
#     my_tuple[1] = 3
# except TypeError:
#     print('Você não pode modificar uma tupla!')

# As tuplas sãouma forma eficaz de usar funções para retornar múltiplos valores:

# In[ ]:


def sum_and_produt (x, y):
    return ( x + y), (x * y)
sum_and_produt(15, 5)



# In[ ]:


s, p = sum_and_produt (5, 10) # s e 15 p e 50


# Dicionarios (Dict)

# In[ ]:


altura = {'Amanda': 1.65, 'Ana': 1.60, 'João': 1.70}
peso = {'Amanda': 65, 'Ana': 86, 'João': 170}

print('A altura do João é:', altura['João'])
print('O peso de Ana é:', peso['Ana'])


# In[ ]:


cadastro {
    'nome': 'Tânia',
    'idade': 35,
    'fruta': 'Uva',
    'cor': 'Roxa',
    'musica': 'Forró'
}
cadastro




# #Podemos editar ou adicionar um valor em um dicionario

# In[ ]:


cadastro ['fruta'] = 'laranja'
cadastro


# In[ ]:





# In[ ]:




