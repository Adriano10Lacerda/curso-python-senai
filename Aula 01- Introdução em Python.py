#!/usr/bin/env python
# coding: utf-8

# Exercício 01 – Crie um programa para receber dois valores e em seguida, exiba o valor
# da soma.
# 

# In[ ]:


valor1 = 10
valor2 = 30
soma = valor1 + valor2
print(soma)


# Exercício 02 – Crie um programa para receber dois valores e em seguida, exiba o valor
# da diferença entre eles.

# In[ ]:


valor1 = 10
valor2 = 5
soma = valor1 - valor2
print(soma)


# Exercício 03 – Crie um programa para receber dois valores e em seguida, exiba o
# produto entre eles.

# In[ ]:


valor1 = 10
valor = 5
produto = valor1 * valor2
print(produto)


# Exercício 04 - Crie um programa para receber dois valores e em seguida, exiba o
# quociente entre eles.

# In[ ]:


valor1 = 10
valor2 = 5
quociente = valor1 / valor2
print(quociente)


# Exercício 05 - Crie um programa para receber dois valores e em seguida, exiba o resto
# da divisão entre eles.

# In[ ]:


valor1 = 10
valor2 = 3
resto = valor1 % valor2

print('O resultado e: ',resto)


# Exercício 06 - Crie um programa para receber um número e em seguida, exiba o
# quadrado dele.

# In[ ]:


valor1 = 5 
quadrado = valor1 ** 2
print('Resultado e: ', quadrado)


# Exercício 07 – Elabora um programa para calcular a raiz quadrada de um número,
# utilizando a biblioteca math.

# In[ ]:


import math
num = 25
raiz_quadrada = math.sqrt(num)
print (raiz_quadrada)


# Exercício 08 – Crie um programa que seja capaz de calcular o valor absoluto de um
# número.

# In[ ]:


num = -5
absoluto = abs(num)
print(absoluto)


# Exercício 10 - Faça um Programa que converta metros para centímetros.

# In[ ]:


n1 = input('Digite valor em metros para converter em centimetros: ')
n1 = int(n1)
type(n1)

centimetros = n1 * 100
print(centimetros)


# Exercício 11 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua
# área.

# In[ ]:


import math
ac = input('Digite diamentro do circulo para calcular area: ')
ac = float(ac)
raio = ac / 2
pi = math.pi
area = raio**2 * pi
print('Area do circulo e: ', area)
print(math.pi)


# 
# Exercício 12 - Faça um Programa que calcule a área de um quadrado, em seguida
# mostre o dobro desta área para o usuário.

# In[14]:


n1 = input('Digite a base do quadrado: ')
n1 = int(n1)
n2 = input('Digite a altura do quadrado: ')
n2 = int(n2)
ar = n1 * n2
db = ar * 2
print('Area do quadrado e igual: ', ar)
print('Dobro da area e: ', db)


# In[16]:


lado = input('Digite o valor refencia ao lado do quadrado')
lado = float(lado)#converter para o numero decimal
areaQuadrado = lado ** 2
dobroArea = areaQuadrado * 2
print('O lado do quadrado é:', lado, 'mm')
print('A area do quadrado é:', areaQuadrado, 'mm²')
print('O dobro da area é:', dobroArea, 'mm²')


# Exercício 13 - Faça um Programa que pergunte quanto você ganha por hora e o número
# de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

# In[20]:


h1=input('Digite quanto vc ganha por hora: ')
h1= float(h1)
h2=input('Digite o total de horas trabalhada no mês: ')
h2= float(h2)
salario = (h1 * h2)
print('Recebendo um valor por hora de R$',h1)
print('Trabalhando',h2, 'horas mês')
print('Seu salario mensal e de:R$',salario)
           


# Exercício 14 - Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.

# In[19]:


n1 = input('Digite a temperatura graus Fahrenheit: °F')
n1 = float(n1)
gc = (n1 - 32) * 5 / 9
gc = float(gc)
type(n1)
print('Temperatura em graus Celsius e: ',gc,'C°')


# Exercício 15 - Faça um Programa que peça a temperatura em graus Celsius, transforme
# e mostre em graus Fahrenheit.

# In[21]:


tc = input('Digite a temperatura em Celsius: ')
tc = float(tc)
tf = (tc * 9 / 5)+32
tf = float(tf)
print('Temperatura em Fahrenheit e: ',tf,'°F')


# In[ ]:




