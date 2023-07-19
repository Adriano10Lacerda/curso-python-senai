#!/usr/bin/env python
# coding: utf-8

# Escreva um programa que solicite ao usuário um número inteiro e verifique se ele é um número positivo. Em seguida, exiba a mensagem correspondente.

# In[1]:


num = int(input('Digite um numero: '))
if num < 0:
    print('negativo')
elif num > 0:
    print('Positivo')
else:
    print('Nulo')


#  Escreva um programa que solicite ao usuário a idade de uma pessoa e verifique se ela é maior de idade (idade igual ou superior a 18) e se possui carteira de motorista. Em seguida, exiba a mensagem correspondente.

# In[3]:


idade = int(input('Digite sua idade: '))
if idade >= 18:
    print('Você é maior de idade!')
else:
    print('Você é menor de idade!')


# Escreva um programa que solicite ao usuário um número inteiro e verifique se ele é um número perfeito. Um número perfeito é aquele cuja soma dos seus divisores (excluindo ele mesmo) é igual ao próprio número. Por exemplo, 6 é um número perfeito, pois seus divisores são 1, 2 e 3, e 1 + 2 + 3 = 6.

# In[5]:


num =int(input('Digite o valor para verificar se e um numero perfeito.'))

#este codigo considera apaenas para o numero 6
soma_divisores = 1

# Verefica se o numero e divisivel por 2
if (num % 2) == 0:
    soma_divisores = soma_divisores + 2
    
# Verifica se o numero e divisivel por 3
if (num % 3) == 0:
    soma_divisores = soma_divisores + 3
if soma_divisores == num:
    print(f'O numero {num} e um numero perfeito.')
else:
    print(f'O numero {num} não e um numero perfeito')


# Escreva um programa que solicite ao usuário um número inteiro e verifique se ele é um número primo. Em seguida, exiba a mensagem correspondente. (Reutilize a questão anterior ou elabore um código diferente).

# In[ ]:



    



# Escreva um programa que solicite ao usuário o nome de um mês e verifique se ele corresponde a um mês de verão (dezembro, janeiro ou fevereiro). Em seguida, exiba a mensagem correspondente.

# In[15]:


mes = input('Digite o mês: ')
if mes.lower() == 'dezembro' or mes.lower() == 'janeiro' or mes.lower() == 'fevereiro':
    print(f'Esse mês {mes} e de verão!!')
else:
    print(f'Esse mês {mes} não e de verão!!')
 


# Escreva um programa que solicite ao usuário um número inteiro e verifique se ele é um quadrado perfeito. Um número é considerado um quadrado perfeito quando sua raiz quadrada é um número inteiro.

# In[17]:


import math

num = int(input('Digite um numero: '))
raiz = math.sqrt(num) # Raiz quadrada
print(raiz)
print(raiz.is_integer())
if raiz.is_integer() == True:
    print('Este numero é um quadrado perfeito!!')
else:
    print('Este número não é um quadrado perfeito!!')
    


# Faça um Programa que leia três números e mostre o maior e o menor deles.

# In[19]:


num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

# verificando o maior numero
if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3
    
# verificando o maior numero
if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3
    
    print('O número maior é ',maior)
    print('O número menor é ',menor)


# In[ ]:




