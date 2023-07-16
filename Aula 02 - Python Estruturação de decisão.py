#!/usr/bin/env python
# coding: utf-8

# ### Exercício 01 
# 
# Crie uma variável chamada "idade" e atribua um valor inteiro a ela. Verifique se a idade é maior ou igual a 18 e imprima "Maior de idade" ou "Menor de idade" de acordo com a condição.

# In[5]:


idade = int(input('Digite sua idade: '))
if idade < 18:
    print('Menor de idade.')
else:
    print('Maior de idade.')


# ### Exercício 02 
# 
# Crie uma variável chamada "número" e atribua um valor inteiro a ela. Verifique se o número é positivo, negativo ou zero e imprima a mensagem correspondente.

# In[8]:


numero = int(input('Digite qualquer numero inteiro: '))
if numero > 0:
    print(f'O numero {numero} é positivo.')
elif numero < 0:
    print(f'O numero {numero} é negativo.')
else:
    print('Nulo')


# ### Exercício 03 
# 
# Crie duas variáveis, "nota1" e "nota2", e atribua valores numéricos a elas. Verifique se a média das notas é maior ou igual a 7 e imprima "Aprovado" ou "Reprovado" de acordo com a condição.

# In[11]:


nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota:'))
media = (nota1 + nota2) / 2
if media <=7:
    print(f'Sua nota é {media} você esta reprovado.')
else:
    print(f'Sua nota é {media} Parabens!! Voce foi aprovado.')


# ### Exercício 04 
# 
# Crie uma variável chamada "idade" e atribua um valor inteiro a ela. Verifique se a idade está dentro do intervalo de 18 a 30 (inclusive) e imprima a mensagem "Idade válida" ou "Idade inválida" de acordo com a condição.

# In[20]:


idade = int(input('Digite uma idade. '))
if  18 <= idade <= 30:
    print(f'Essa idade {idade} é uma idade valida.')
else:
    print(f'Essa idade {idade} é invalida.')


# ### Exercício 05 
# 
# Crie uma variável chamada "numero" e atribua um valor inteiro a ela. Verifique se o número é par ou ímpar e imprima a mensagem correspondente.

# In[23]:


numero = int(input('Digite um numero interio. '))
if numero % 2 == 0:
    print(f'Esse numero {numero} é par.')
else:
    print(f'Esse numero {numero} é impar.')


# ### Exercício 06 
# 
# Crie uma variável chamada "horario" e atribua um valor inteiro representando a hora do dia (em formato 24 horas). Verifique se o horário está dentro do período da manhã (das 6h às 12h), da tarde (das 12h às 18h) ou da noite (das 18h às 23h) e imprima a mensagem correspondente.

# In[2]:


horario = int(input('Digite uma hora. '))
if  6 <= horario < 12:
    print('Bom dia!!')
elif 12 <= horario < 18:
    print('Boa tarde!!')
elif 18 <= horario < 23:
    print('Boa noite!!')
elif 0 <= horario < 6:
    print('Boa madrugada!!')
else:
    print('Nulo!!')


# ### Exercício 07 
# 
# Crie uma variável chamada "peso" e atribua um valor numérico a ela. Verifique se o peso está dentro do intervalo de 50 a 100 (inclusive) e imprima a mensagem "Peso válido" ou "Peso inválido" de acordo com a condição.

# In[16]:


peso = float(input('Digite seu peso. '))
if 50  <= peso <=  100:
    print('Peso válido!')
else:
    print('Valor inválido!')


# ### Exercício 08 
# 
# Crie uma variável chamada "numero" e atribua um valor inteiro a ela. Verifique se o número é múltiplo de 3 e de 5 ao mesmo tempo e imprima a mensagem correspondente.

# In[20]:


numero = int(input('Digite numero: '))
if numero % 3 == 0 and numero % 5 == 0:
    print(f'O número {numero} e multiplo de 3 e 5. ')
else:
    print(f'O número {numero} não e multiplo de 3 e 5')
    


# ### Exercício 09 
# 
# Crie uma variável chamada "ano" e atribua um valor inteiro representando um ano. Verifique se o ano é bissexto (divisível por 4, mas não por 100, exceto se for divisível por 400) e imprima a mensagem correspondente.

# In[22]:


ano = int(input('Digite o ano: '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} e bissexto!!')
else:
    print(f'O ano {ano} não e bissexto!!')


# ### Exercício 10 
# 
# Crie uma variável chamada "salario" e atribua um valor numérico a ela. Verifique se o salário é maior do que 1000 e menor do que 2000 ao mesmo tempo e imprima a mensagem correspondente.

# In[8]:


salario = float(input('Digite seu salario:R$'))
if 1000 <= salario <=  2000:
    print(f'O seu salario {salario} segue o padrão.')
else:
    print(f'O seu salario {salario} não segue o padrão.')
    
    


# ### Exercício 11 
# 
# Faça um Programa que peça dois números e imprima o maior deles.

# In[10]:


num1 = int(input('Digite primeiro numero: '))
num2 = int(input('Digita segundo numero: '))
if num1 > num2:
    print(f'O primeiro número {num1} e maior que o segundo número!!')
else:
    print(f'O segundo número {num2} e maior que o primeiro número!!')


# ### Exercício 12 
# 
# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

# In[15]:


num = int(input('Digite um numero inteiro: '))
if 0 < num:
    print(f'O número {num} e positivo !! ')
elif 0 > num:
    print(f'O número {num} e negativo !!')
else:
    print(f'O numero {num} e nulo !!')


# ### Exercício 13 
# 
# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

# In[20]:


letra = input('Digite seu sexo F Feminino e M Masculino.')
if letra == 'F' or letra == 'f':
    print(f'O sexo seu e Feminino.')
elif letra == 'M' or letra == 'm':
    print(f'O seu sexo seu e Masculino.')
else:
    print('Sexo Inválido')


# ### Exercício 14 
# 
# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

# In[24]:


letra = input( 'Digite uma letra:')
if letra.lower() in ['a','e','i','o','u']:
    print(f'A letra digitada {letra} e uma vogal.')
else:
    print(f'A letra digitada {letra} e uma consoante.')
    


# ### Exercício 15 
# 
# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# 
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# 
# A mensagem "Reprovado", se a média for menor do que sete;
# 
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

# In[28]:


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
if media == 10:
    print('Aprovado com Distinção')
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado')


# In[ ]:




