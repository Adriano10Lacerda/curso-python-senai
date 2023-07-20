#!/usr/bin/env python
# coding: utf-8

# ### Exercício 01 
# Crie uma lista com nomes de 4 times de futebol.
# 
# a) Palmeiras
# b) São Paulo
# c) Santos
# d) Água Santa
# e) Acesse o time que está na 3a posição.
# f) Crie uma lista com duas listas de 3 times de futebol, cada uma de uma
# divisão diferente.

# In[1]:


times = ['Palmerias', 'São Paulo', 'Santos', 'Àgua Santa']
times [2]


# In[2]:


# f) Crie uma lista com duas listas de 3 times de futebol, cada uma de uma divisão diferente.
divisao = [['Palmerias', 'São Paulo', 'Santos',],['Crb', 'Londrina', 'cruzeiro']]
#para buscar a listas dentro de listas, o primeiro colchete e para a lista que deseja e segunda lista e posição.
divisao [1][0]




# ### Exercício 02 
# Crie uma lista com 3 diferentes moedas. Acrescente mais 2
# outras moedas à essa mesma lista.

# In[15]:


moedas = ['Real', 'Cruzeiro', 'Urv']

moedas.append('Inhei')
moedas


#Transformar a lista em uma string
moedas = ',' .join(moedas)
type(moedas)



# In[16]:


#Converter uma string em lista
moedas = moedas.split(',')
type(moedas)


# In[ ]:





# In[ ]:




