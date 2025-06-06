

#tuplas
#elas são imutáveis e não podem ser alteradas
#não podem ser removidos items,adicionados ou modificados em uma tupla
#declaração implícita não é necessário declarar o tipo 

'''
got=("Game of Thrones",2011,2019,9.4)
print(got)
print(type(got))
print(len(got))
'''

#declaração explícita 
'''
got=tuple(["game of thrones",2011,2019,9.4])
print(got)
print(type(got))
print(len(got))
'''
#verificando dados dentro de uma tupla
'''
top5=("black mirror","breakind bad","friends","game of thrones")
print("house"in top5)
print("game of thrones"in top5)
'''

#posições na tupla index
'''
empresas=("Brasil","EUA","Canadá","Rússia")
print(empresas.index("Brasil"))
'''

#matrizes 

#são identificadas por dados com um par de indíces que idicam sua posição
#elemento está em tal coluna e tal linha 
'''
matriz=[[1,2,3],[5,6,7]]
print(matriz[0][0])
'''

'''
#exemplo

matriz=[[1, 2, 3], #0
        [5, 6, 7]] #1

        #0 #1 #2
'''



#inicializar a matriz

#pedir ao usuário as dimensões da matriz
'''
n=int(input("digite o número de linhas da matriz"))
m=int(input("digite o número de colunas da matriz"))


#passo 2 

i=0

matriz=[]

while i<n:
    linha=[]
    j=0
    while j<m:
        linha.append(0)
        j+=1
        matriz.append(linha)

'''
'''

numeros=[]


for i in range(5):
    numero=int(input("digite um número:"))
    numeros.append(numero)


tupla=tuple(numeros)

media=sum(tupla)/len(tupla)

print(f"A média é:,{media}")
'''





'''

numeros=[]


for i in range(5):
    numero=int(input("digite um número:"))
    numeros.append(numero)


tupla=tuple(numeros)

media=sum(tupla)/len(tupla)
'''




'''
numeros=[]



for i in range(5):
    numero=int(input("digite um número:"))
    numeros.append(numero)

tupla=tuple(numeros)

media=sum(tupla)/len(tupla)


print(f"a média dos números é:{media}")
'''





'''
numeros=[]


for i in range(5):
    numero=int(input("digite um número:"))
    numeros.append(numero)


tupla=tuple(numeros)


media=sum(tupla)/len(tupla)



print(f"a média é:{media}")

'''


'''

numeros=[]


for i in range(5):
    numero=int(input("digite um número:"))
    numeros.append(numero)

tupla=tuple(numeros)


media=sum(tupla)/len(tupla)


print(f"a média é :{media}")
'''





    


'''
numeros=[]


for i in range(5):
    numero=int(input("digite um número:"))
    numeros.append(numero)


tupla=tuple(numeros)

media=sum(tupla)/len(tupla)

'''


numeros=[]


for i in range(5):
    numero=int(input("digite um número :"))
    numeros.append(numero)


tupla=tuple(numeros)

media=sum(tupla)/len(tupla)


print(f"{media}")







