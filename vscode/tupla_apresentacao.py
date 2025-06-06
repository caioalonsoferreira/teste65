

'''

#Crie uma matriz 2x3
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

# Some os elementos da primeira linha
soma_primeira_linha = sum(matriz[0])
print(soma_primeira_linha)
'''



#exercício tupla 




numeros = (10, 20, 30, 40, 50)
soma = 0
contador = 0

for num in numeros:
    soma += num
    contador += 1

media = soma / contador
print(f"Média: {media}")



'''
tupla = (1, 2, 3, 2, 4, 5, 3)
sem_repetidos = ()  # Cria uma tupla vazia onde vamos armazenar os elementos únicos

for num in tupla:  # Itera sobre cada elemento da tupla
    if num not in sem_repetidos:  # Verifica se o número já foi adicionado à tupla 'sem_repetidos'
        sem_repetidos += (num,)  # Se não, adiciona o número à tupla 'sem_repetidos'

print(sem_repetidos)  # Exibe a tupla sem os números repetidos

'''



