'''
while True:
    n1 = int(input("Digite a primeira nota, entre 0 a 10: "))
    n2 = int(input("Digite a segunda nota, entre 0 a 10: "))

    # Verifica se as notas estão no intervalo correto (0 a 10)
    if n1 not in range(0, 11):  # Corrigido para incluir o número 10
        print("Número inválido! Digite novamente.")
        continue  # Continua o loop sem sair
    if n2 not in range(0, 11):  # Corrigido para incluir o número 10
        print("Número inválido! Digite novamente.")
        continue  # Continua o loop sem sair

    # Calcula a média das notas
    resultado = (n1 + n2) / 2
    print(f"O resultado da conta é: {resultado}")
    break  # Sai do loop após calcular as notas válidas
'''


'''
while True:
   usuario = input("Digite o nome de usuário: ")
   senha = input("Digite a senha: ")
   # Verifica se a senha é igual ao nome do usuário
   if senha == usuario:
       print("Erro: A senha não pode ser igual ao nome de usuário.")
   else:
       break  # Sai do loop se a senha for válida
tentativas = 0
# Valida a senha pedindo para digitar novamente
while tentativas < 12:
   senha_repetida = input("Digite a senha novamente para confirmar: ")
   if senha_repetida == senha:
       print("Senha validada com sucesso!")
       break  # Sai do loop se a senha repetida for correta
   else:
       tentativas += 1
       print(f"Senha incorreta. Tentativas restantes: {12 - tentativas}")
if tentativas == 12:
   print("Número de tentativas excedido. O programa será encerrado.")

'''

'''
numero=int(input("digite um número de 1 a 10 para ver a tabuada:"))

if  1<= numero <=10:
    print(f"tabuada do número {numero}:")

    for i in range(1,11):
        print(f"{numero} X {i} = {numero*i}")


else:
    print("número errado digite o número entre as condições")
'''
'''
numeros=[1,2,3.4,5]

soma=1+2+3+4+5

media=(1+2+3+4+5)/5

print(f"o resultado da soma dos números é: {soma}")
print(f"o maior numero é :",max(numeros))
print(f"a média dos resultados é:{media}")
'''



'''

nome=input("digite seu nome:")
 
while len(nome)<3:
    print("o nome tem que ser maior que três caracteres")
    nome=input("digite seu nome:")
 
idade=int(input("digite a sua idade:"))
 
while idade<0 or idade >150:
    print("idade tem que ser entre 0 a 150!")
    idade=int(input("digite a sua idade:"))
 
salario=int(input("digite o seu salário:"))
 
while salario <0:
    print("salário tem que ser maior que 0")
    salario=int(input("digite o seu salário:"))
 
genero=input("digite seu genero (m),(f),ou (o):")
 
while genero.lower() not in ['m','f','o']:
    print("gênero selecionado não encontrado!")
    genero=input("digite seu genero (m),(f),ou (o):")
 
estado=input("digite seu estado civil(s),(c),(v),(d):")
 
while estado.lower() not in ['s','c','v','d']:
    print("estado civil não encontrado!")
    estado=input("digite seu estado civil(s),(c),(v),(d):")
 
 
print(f"o seu nome é:{nome}")
print(f"a sua idade é:{idade}")
print(f"o seu salário é:{salario}")
print(f"o seu gênero é:{genero}")
print(f"o seu estado civil:{estado}")
'''
 



'''
populacao_a=8000
populacao_b=200000
 
crescimento_a=0.3
crescimento_b=0.015
 
anos=0
 
while populacao_a<populacao_b:
    populacao_a+=populacao_a*crescimento_a
    populacao_b+=populacao_b*crescimento_b
    anos+=1
 
print(f"será necessário {anos} anos para ultrapassar a população do páis B")
'''


'''
soma=0
 
while True:
    numero=int(input("digite um número positivo para finalizar:"))
 
    if numero< 0:
        print("número inválido, digite um número positivo:")
        continue
 
 
    if numero==0:
        print(f"a soma dos números é:{soma}")
        break
 
 
    soma+=numero
'''



'''
notas = []

while len(notas)<4:
    nota =float(input("digite uma nota entre 0 a 10, ao digitar -1 o programa se encerra:"))

    if nota == -1:
        break

    if nota < 0  or nota > 10:
       print("Erro,digite um número entre 0 a 10 :")
    else:
        notas.append(nota)
    
if notas:
    print(f"Você inseriu {len(notas)} notas válidas. A média das notas é: {sum(notas)/len(notas):.1f}")
else:
    print("Valor invalido!,digite outro número ")
    
'''

#print(f"{sum(notas)/ len(notas):.1f}")

# Inicializando as variáveis para contar os votos



#exercício 9

'''''''''
votos_candidato_1 = 0
votos_candidato_2 = 0
votos_candidato_3 = 0
votos_candidato_4 = 0
votos_nulos = 0
votos_brancos = 0
while True:
   # Lê o código do voto
   voto = int(input("Digite o código do voto (1, 2, 3, 4, 5, 6) ou 0 para encerrar: "))
   # Condição de parada
   if voto == 0:
       break
   # Contabilizando os votos
   elif voto == 1:
       votos_candidato_1 += 1
   elif voto == 2:
       votos_candidato_2 += 1
   elif voto == 3:
       votos_candidato_3 += 1
   elif voto == 4:
       votos_candidato_4 += 1
   elif voto == 5:
       votos_nulos += 1
   elif voto == 6:
       votos_brancos += 1
   else:
       print("Código de voto inválido. Tente novamente.")
# Exibindo os resultados
print("\nResultado final da eleição:")
print(f"Candidato 1: {votos_candidato_1} votos")
print(f"Candidato 2: {votos_candidato_2} votos")
print(f"Candidato 3: {votos_candidato_3} votos")
print(f"Candidato 4: {votos_candidato_4} votos")
print(f"Votos nulos: {votos_nulos} votos")
print(f"Votos em branco: {votos_brancos} votos")
'''



cand_1=0
cand_2=0
cand_3=0
cand_4=0

votos_nulos=0
voto_branco=0

while True:
    votos=int(input("digite um voto entre 0 a 6"))

    if votos==1:
        cand_1+=1
    
    elif votos==2:
        cand_2+=1

    elif votos==3:
        cand_3+=1


    elif votos==4:
        cand_4+=1


    elif votos==5:
        votos_nulos+=1


    elif votos==6:
        voto_branco+=1


    elif votos==0:
        break    


    else:

        print("Código de voto inválido. Tente novamente.")
    

    

