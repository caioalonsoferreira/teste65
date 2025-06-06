
'''
# Função para exibir números pares e ímpares
def exibir_pares_impares(n):
    print(f"\nNúmeros entre 1 e {n}:")

    # Usando o while para exibir pares
    print("Pares:")
    i = 2
    while i <= n:
        print(i, end=" ")
        i += 2

    # Usando o for para exibir ímpares
    print("\nÍmpares:")
    for i in range(1, n + 1, 2):
        print(i, end=" ")

# Função para calcular a soma
def somar_numeros(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma

# Entrada de dados do usuário
numero = int(input("Digite um número: "))

# Soma dos números
soma = somar_numeros(numero)

# Exibindo os resultados
print(f"\nA soma de todos os números de 1 até {numero} é: {soma}")

# Exibindo os números pares e ímpares
exibir_pares_impares(numero)
'''



# Função para a contagem regressiva
def contagem_regressiva(n):
    print(f"\nContagem regressiva de {n} até 0:")
    while n >= 0:
        print(n, end=" ", flush=True)
        n -= 1

# Função para exibir múltiplos de 3
def multiplos_de_3(n):
    print(f"\nMúltiplos de 3 entre 1 e {n}:")
    for i in range(1, n + 1):
        if i % 3 == 0:
            print(i, end=" ")

# Entrada de dados do usuário
numero = int(input("Digite um número para iniciar a contagem regressiva: "))

# Chama a função para a contagem regressiva
contagem_regressiva(numero)

# Chama a função para exibir múltiplos de 3
multiplos_de_3(numero)

