
'''
def quadrado (numero):

    return numero*numero

print(quadrado(10))

'''
'''
def boasvindas(nome):
    print(f"olá,{nome}!")

boasvindas("caio")

'''
'''
def multiplo_de(numero,multiplo):

    resultado=numero%multiplo==0

    print(f"{numero} é multiplo de {multiplo}?",end=" ")
    print(resultado)


multiplo_de(18,9)

'''
'''
def imprimequadrado(numero):
    if numero ==1:
        return
    print("%d\t"%(numero*numero))

imprimequadrado(10)

'''
'''

def exibemenu():
    print("#### menu ###\n")
    print("0-SAIR\n")
    print("1-SOMAR\n")
    print("2-SUBTRAIR\n")
    print("3-MULTIPLICAR\n")
    print("4-DIVIDIR\n")

    opcao=int(input("escolha uma das opções:"))
    return opcao

def calcular(operacao, num1, num2):
    if operacao == 'soma':
        resultado= num1 + num2
    elif operacao == 'subtracao':
        resultado= num1 - num2
    elif operacao == 'multiplicacao':
        resultado= num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
           
         return operacao
    

i=0
opcao=1
num1=0
num2=0
resultado=0

while opcao!=0:
    opcao=exibemenu()
    if opcao <=0:
        break

    num1=float(input("informe o primeiro numero para a operação:"))
    num2=float(input("informe o primeiro numero para a operação:"))

    if opcao==1:
        resultado=calcular(num1,num2)

    print("resultado:%f\n\n"%resultado)

'''



'''
def exibemenu():
    print("#### MENU ####")
    print("0 - SAIR")
    print("1 - SOMAR")
    print("2 - SUBTRAIR")
    print("3 - MULTIPLICAR")
    print("4 - DIVIDIR")
    
    opcao = int(input("Escolha uma das opções: "))
    return opcao

def calcular(operacao, num1, num2):
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: divisão por zero"
    else:
        return "Operação inválida"

# Programa principal
opcao = 1  # Inicia com valor diferente de 0
while opcao != 0:
    opcao = exibemenu()
    
    if opcao == 0:
        print("Saindo do programa.")
        break
    
    num1 = float(input("Informe o primeiro número: "))
    num2 = float(input("Informe o segundo número: "))
    
    if opcao == 1:
        resultado = calcular('soma', num1, num2)
    elif opcao == 2:
        resultado = calcular('subtracao', num1, num2)
    elif opcao == 3:
        resultado = calcular('multiplicacao', num1, num2)
    elif opcao == 4:
        resultado = calcular('divisao', num1, num2)
    else:
        resultado = "Opção inválida"
    
    print("Resultado: {}\n".format(resultado))

'''

'''

def exibeopcoes():
    print("##### MENU #####")
    print("1- Acender a lampada")
    print("2- Apagar a lampada")
    print("3- Exibir status")

    opcao=int(input("digite uma opção:"))
    return opcao

    
    
    
    
def opcao():

    if opcao==1:
        print("lampada acessa")
        return opcao
    

    elif opcao ==2:
        print("lampada desligada")


    elif opcao ==3:
        print("o estado atul é ")

'''


    

'''
def exibe_opcoes():
    print("\n##### MENU #####")
    print("1 - Acender a lâmpada")
    print("2 - Apagar a lâmpada")
    print("3 - Exibir status da lâmpada")
    print("4 - Sair")

    opcao = int(input("Digite uma opção: "))
    return opcao


def executa_opcao(opcao, estado):
    if opcao == 1:
        estado = "acesa"
        print("A lâmpada foi acesa.")
    elif opcao == 2:
        estado = "apagada"
        print("A lâmpada foi apagada.")
    elif opcao == 3:
        print(f"O estado atual da lâmpada é: {estado}")
    else:
        print("Opção inválida!")
    return estado


# Programa principal
estado_lampada = "apagada"
while True:
    escolha = exibe_opcoes()
    if escolha == 4:
        print("Saindo do programa.")
        break
    estado_lampada = executa_opcao(escolha, estado_lampada)

'''



'''

def exibe_opcoes():


    print("###### MENU #####")
    print("1- Acender lampada")
    print("2- Apagar lampada")
    print("3- Exibir status da lampada ")
    print("4- Sair")

    opcao=int(input("digite a opção:"))
    return opcao


def executa_opcao(opcao,estado):
    
    if opcao ==1:
    estado="acessa"
        print("a lampada foi acessa")

'''



'''
def exibe_opcoes():
    print("\n##### MENU #####")
    print("1 - Acender a lâmpada")
    print("2 - Apagar a lâmpada")
    print("3 - Exibir status da lâmpada")
    print("4 - Sair")
 
    opcao = int(input("Digite uma opção: "))
    return opcao
 
 
def executa_opcao(opcao, estado):
    if opcao == 1:
        estado = "acesa"
        print("A lâmpada foi acesa.")
    elif opcao == 2:
        estado = "apagada"
        print("A lâmpada foi apagada.")
    elif opcao == 3:
        print(f"O estado atual da lâmpada é: {estado}")
    else:
        print("Opção inválida!")
    return estado
 
 
# Programa principal
estado_lampada = "apagada"
while True:
    escolha = exibe_opcoes()
    if escolha == 4:
        print("Saindo do programa.")
        break
    estado_lampada = executa_opcao(escolha, estado_lampada)
 
'''



'''
def exibemenu():
    print("#### MENU ####")
    print("0 - SAIR")
    print("1 - SOMAR")
    print("2 - SUBTRAIR")
    print("3 - MULTIPLICAR")
    print("4 - DIVIDIR")
    
    opcao = int(input("Escolha uma das opções: "))
    return opcao

def calcular(operacao, num1, num2):
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: divisão por zero"
    else:
        return "Operação inválida"

# Programa principal
opcao = 1  # Inicia com valor diferente de 0
while opcao != 0:
    opcao = exibemenu()
    
    if opcao == 0:
        print("Saindo do programa.")
        break
    
    num1 = float(input("Informe o primeiro número: "))
    num2 = float(input("Informe o segundo número: "))
    
    if opcao == 1:
        resultado = calcular('soma', num1, num2)
    elif opcao == 2:
        resultado = calcular('subtracao', num1, num2)
    elif opcao == 3:
        resultado = calcular('multiplicacao', num1, num2)
    elif opcao == 4:
        resultado = calcular('divisao', num1, num2)
    else:
        resultado = "Opção inválida"
    
    print("Resultado: {}\n".format(resultado))


'''

'''
def exibe_opcoes():
    print("#### MENU ####")
    print("1-acender a lampâda")
    print("2-apagar a lampâda")
    print("3-exibir status da lampâda")
    print("4-Sair")

    opcao=int(input("digite uma opção:"))
    return opcao

def executa_opcao(opcao,estado):

    if opcao == 1:
        estado="acessa"
        print("a lampâda foi acessa")

    elif opcao==2:
        estado="apagada"
        print("a lampâda foi apagada")

    elif opcao==3:
        print(f"o estado atual da lampâda é:{estado}")

    else:
        print("opção inválida")

        return estado
    



estado_lampada="apagada"

while True:

    escolha=exibe_opcoes()
    if escolha==4:
        print("Saindo do programa")
        break

    estado_lampada=executa_opcao(escolha,estado_lampada)

'''
'''

gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
maior_nota = 0
menor_nota = 10  
total_alunos = 0
soma_notas = 0

while True:
    acertos = 0
    print(f"Aluno {total_alunos + 1}, insira suas respostas:")
    
    for i in range(10):
        resposta = input(f"Questão {i+1}: ").strip().upper()
        if resposta == gabarito[i]:
            acertos += 1
    
    
    for i in range(1,11):
        resposta = input(f"Questão {i}: ").strip().upper()

        if (i == 1 and resposta == 'A') or \
        (i == 2 and resposta == 'B') or \
        (i == 3 and resposta == 'C')or \
        (i == 4 and resposta == 'D')or \
        (i == 5 and resposta == 'E')or \
        (i == 6 and resposta == 'E')or \
        (i == 7 and resposta == 'D')or \
        (i == 8 and resposta == 'C')or \
        (i == 9 and resposta == 'B')or \
        (i == 10 and resposta == 'A'):
            acertos += 1
    
    if input("Questão 1: ").strip().upper() == 'A': acertos += 1 
    if input("Questão 2: ").strip().upper() == 'B': acertos += 1 
    if input("Questão 3: ").strip().upper() == 'C': acertos += 1 
    if input("Questão 4: ").strip().upper() == 'D': acertos += 1 
    if input("Questão 5: ").strip().upper() == 'E': acertos += 1 
    if input("Questão 6: ").strip().upper() == 'E': acertos += 1 
    if input("Questão 7: ").strip().upper() == 'D': acertos += 1 
    if input("Questão 8: ").strip().upper() == 'C': acertos += 1 
    if input("Questão 9: ").strip().upper() == 'B': acertos += 1 
    if input("Questão 10: ").strip().upper() == 'A': acertos += 1 


    print(f"Nota do aluno: {acertos}")
    

    total_alunos += 1
    soma_notas += acertos
    if acertos > maior_nota:
        maior_nota = acertos
    if acertos < menor_nota:
        menor_nota = acertos

    #opção 1
    maior_nota = max(maior_nota, acertos)
    menor_nota = min(menor_nota, acertos)
    
    continuar = input("Outro aluno vai utilizar o sistema? (S/N): ").strip().upper()
    if continuar != 'S':
        break

if total_alunos > 0:
    media_notas = soma_notas / total_alunos
    print(f"\nMaior Acerto: {maior_nota}")
    print(f"Menor Acerto: {menor_nota}")
    print(f"Total de Alunos que utilizaram o sistema: {total_alunos}")
    print(f"Média das Notas da Turma: {media_notas:.2f}")
else:
    print("Nenhum aluno utilizou o sistema.")


'''


'''
def obter_respostas():

    respostas=[]

    for i in range(10):
        while True:
            resposta=input(f"Questão {i+1}(A,B,C,D,ou E):").strip().upper()
            if resposta in['A','B','C','D','E']:
                respostas.append(resposta)
                break

            print("Resposta inválida. Tente novamente.")
        return respostas
    
def corrigir_prova(respostas_aluno,gabarito):

        acertos=0
        for i in range(len(gabarito)):
            if respostas_aluno[i]==gabarito[i]:
                acertos+=1

        return acertos
    
def perguntar_continuar():
     return input("Outro aluno ?(S/N):").strip().upper()=='S'


def mostrar_resultados(notas):
     
     print(f"total de alunos:{len(notas)}")
     print(f"O maior acerto:{max(notas)}")
     print(f"O menor acerto:{min(notas)}")
     print(f"Média:{sum(notas)/len(notas)}")


gabarito=["A","B","C","D","E","E","D","C","B","A"]
notas=[]


while True:
     
     respostas=obter_respostas()
     nota=corrigir_prova(respostas,gabarito)
     notas.append(nota)
     print(f"Você acertou {nota}de 10 questões.")


     if not perguntar_continuar():
          break
     

mostrar_resultados(notas)
     

'''




 