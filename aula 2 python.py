#!/usr/bin/env python
# coding: utf-8

# ### Exercício 16 
# 
# Faça um Programa que leia três números e mostre o maior deles.

# In[9]:


num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))

# avaliando num1

if (num1 > num2) and (num2 > num3):
    if num2 > num3:
        print('----------------------------------')
        print('O primeiro e valor maior é:', num1)
        print('O Segundo e valor maior é:', num2)
        print('O Terceiro e valor maior é:', num3)
        print('----------------------------------')
    else:
        print('----------------------------------')
        print(f'O primeiro e valor maior é:', num1)
        print(f'O Segundo e valor maior é:', num3)
        print('O Terceiro e valor maior é:', num2)
        print('----------------------------------')
elif (num2 > num1) and (num2 > num3): # Avaliando o num 2
    if num1 > num3:
        print('----------------------------------')
        print('O primeiro e valor maior é:', num2)
        print('O Segundo e valor maior é:', num1)
        print('O Terceiro e valor maior é:', num3)
        print('----------------------------------')
    else:
        print('----------------------------------')
        print('O primeiro e valor maior é:', num2)
        print('O Segundo e valor maior é:', num3)
        print('O Terceiro e valor maior é:', num1)
        print('----------------------------------')
elif (num3 > num1) and (num3 > num2):# Avaliando o numero 3
    if num1 > num2:
        print('----------------------------------')
        print('O primeiro e valor maior é:', num3)
        print('O Segundo e valor maior é:', num1)
        print('O Terceiro e valor maior é:', num2)
        print('----------------------------------')
    else:
        print('----------------------------------')
        print('O primeiro e valor maior é:', num3)
        print('O Segundo e valor maior é:', num2)
        print('O Terceiro e valor maior é:', num1)
        print('----------------------------------')


# ### Exercício 17 
# 
# Faça um Programa que leia três números e mostre o maior e o menor
# deles.

# In[21]:


num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))
maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
print('------------------------')
print('O maior numero é: ', maior)
print('O menor numero é: ', menor)



# ### Exercício 18 
# 
# Faça um programa que pergunte o preço de três produtos e informe qual
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

# In[22]:


prec1 = float(input('Digite o primeriro preço:R$'))
prec2 = float(input('Digite o segundo preço:R$'))
prec3 = float(input('Digite o terceiro preço:R$'))
maior = max(prec1, prec2, prec3)
menor = min(prec1, prec2, prec3)
    print('----------------------')
    print('O maior preço é R$',maior,'')


# ### Exercício 21  
# 
# As Organizações Tabajara resolveram dar um aumento de salário aos
# seus colaboradores e lhe contaram para desenvolver o programa que calculará os
# reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste
# segundo o seguinte critério, baseado no salário atual:
# 
# • salários até R$ 280,00 (incluindo) : aumento de 20%
# • salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# • salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# • salários de R$ 1500,00 em diante : aumento de 5%
# 
# Após o aumento ser realizado, informe na tela:
# 
# • salário antes do reajuste;
# • percentual de aumento aplicado;
# • valor do aumento;
# • novo salário, após o aumento.

# In[ ]:


print('---Cálculo de aumento de salario 2023---')
salario = float(input('Informe seu salario:R$'))

print('----------------------------------------')
# definindo o valor do aumento
if salario <= 280:
    
    aumento = 0.2
    
elif (salario > 280) and (salario <=700):
    aumento = 0.15
elif (salario > 700) and (salario <=1500):
    aumento = 0.1
else:
    aumento = 0.05
#--------------------------------------Calculando valor do aumento e novo 

valor_aumento = salario * aumento
novo_salario = salario


