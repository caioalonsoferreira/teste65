
#exercício 1
'''
tupla=(1,2,3,4,5,6,7,8,0)

if 0 in tupla:
    print("zero encontrado")

else:
    print("zero não encontrado")

'''
#exércicio 2
'''
tupla=(3,6,2,9,1,7,5)

maior=tupla[0]


for numero in tupla:
   if numero>maior:
    maior=numero

print(maior)

'''


#exércicio 3
'''
tupla=(1,2,3,4,5,6,7,8)

for num in tupla:
    if num %2==0:
        print(num)

'''

#exercício 4

'''
tupla=(1,2,3,4,5,6,7,8)

soma=0

for num in tupla:
    
    if num %2==0:
        soma+=num

print(soma)

'''

#exercício 5
'''
tupla=(1,2,3,4,5,6,7,8)

for num in tupla:
    if num>5:
        print(num)
        

'''
'''
#exercício 6

alunos=[("João",8.0),("Maria",9.5),("Pedro",7.5),("Ana",8.5)]

maior_nota=alunos[0][1]
aluno_maior_nota=alunos[0][0]

for aluno in alunos:
    nome,nota=aluno

    if nota>maior_nota:
        maior_nota=nota
        aluno_maior_nota=nome

        
        
print(aluno_maior_nota)
'''

'''


#exercício 7
matriz= [[1,2,3],[4,5,6],[7,8,9]]

soma=0

for linha in matriz:
        for valor in linha:
                soma +=valor
                
    
      

print(soma)

'''




'''

# Tuplas de exemplo
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

# Concatenando as tuplas
tupla_concatenada = tupla1 + tupla2

# Exibindo o resultado
print("Tupla concatenada:", tupla_concatenada)
'''




'''
# Atribuindo valores a variáveis de forma implícita em uma tupla
a, b, c = 10, 20, 30

print(a)  # Saída: 10
print(b)  # Saída: 20
print(c)  # Saída: 30
'''


'''

m=[
   [1,2,],
   [3,4],
   [5,6]]


a=[
    [1,3,5],
    [2,4,6]]

print(a)
'''

'''
matriz=[[1,2,11,13],[4,15,16,60],[7,8,19,200],[20,100,5,3]]


contador=0

for linha in matriz:
    for valor in linha:
        if valor>10:
            contador+=1

print(contador)



matriz=[]

contador=0


for linha in matriz:
    for valor in matriz:
        if valor>10:
            contador+=1


'''

'''
matriz_a=[[1,2,3],
          [4,45,67],
          [7,80,9]]



matriz_b=[[100,8,7],
          [6,5,4],
          [3,25,10]]



calculo=matriz_a and  matriz_b

for i in calculo:
    

'''



