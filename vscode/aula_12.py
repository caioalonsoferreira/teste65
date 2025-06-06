# operadores in e not in 
# strings são interáveis e por isso é possível acessar através do in e not in 
'''
nome= 'Caio'
print(nome{-3})

print('io' in nome)
print('io' not in nome)
'''
'''
a=int(input("digite o primeiro lado:"))
b=int(input("digite o segundo lado:"))
c=int(input("digite o terceiro lado:"))
       
condicao1= (a+b>c)
condicao2=(a+c>b)
condicao3=(b+c>a)

if condicao1 and condicao2 and condicao3:
    print("os lados formam um triângulo")
else:
    print("os valores não formam um triângulo válido")    

'''
'''
senha=input("digite uma senha:")

possui_caractres= len (senha)>=8
tem_letramaiscula= senha!= senha.lower()
numero = any(map(str.isdigit, senha))
               
if possui_caractres and tem_letramaiscula and numero:
    print("senha válida")
else:
    print("senha inválida")

'''



'''
idade=int(input("digite a sua idade:"))

if idade<16:
    resultado=("não pode votar")
elif idade ==16 or idade ==17 or idade >70:
    resultado=("voto é opcional")
elif idade>= 18 and idade<=70:
    resultado=("voto obrigatório")
else:
    resultado=("o usuário não pode votar")  
print(f"o partcipante {resultado}")      
'''
'''
n1=int(input("digite a sua nota:"))
print(n1)

while (n1<0) or (n1>10):
    print("a nota deve estar dentro dos padrões")
    n1=int(input("digite novamente:"))

'''


'''
a=int(input("digite o valor:"))
b=int(input("digite o valor:"))
c=int(input("digite o valor:"))

condicao1= a+b>c
condicao2= b+c>a
condicao3= a+c>b

if condicao1 and condicao2 and condicao3:
    resultado="forma um triângulo"
else:
    resultado="não formam um triângulo"

print(f"os lados {resultado}")        
'''
'''
senha=input("digite a sua senha:")

tem_8_caracteres= len (senha)>=8
tem_letra_maiscula=any(map(str.isupper,senha))
tem_numero=any(map(str.isdigit,senha))

if tem_8_caracteres and tem_letra_maiscula and tem_numero:
    resultado="requisitos atendidos"
else:
    resultado="requisitos não atendidos"

print(f"a sua senha está com {resultado}")
'''

'''
n1=float(input("digite a nota :"))
n2=float(input("digite a nota :"))
n3=float(input("digite a nota :"))

frequencia=float(input("digite a sua frequencia:"))
media=(n1+n2+n3)/3

if media>=7:
    resultado="aprovado"

elif media<7:
    resultado="reprovado"

elif media>= 5 and frequencia>=75:
    
    resultado="aprovado"


print(f"o aluno está {resultado}")
'''




'''
#exercício do nome 
while True:
    usuario=input("digite seu nome:")

    if len(usuario) > 5:
        print("erro")
        continue
    if not usuario[0].isalpha():
        print("erro")
        continue #pede para o usúario digitar novamente


    valido = True

    for c in usuario:
        if not (c.isalpha() or c.isdigit()):
            valido= False

            break #sai do loop
    if not valido:
        print("erro:o nome de usuário deve conter apenas numeros e letras")
        continue
    print(f"Nome do usuario {usuario} cadastrado com sucesso!")

    break

'''

while True:
    
    n1=input(input("digite um número:"))
    n2=input(input("digite um número:"))
    
    calculadora=(input("digite uma das seguntes operações +,-,*,/"))

    a=n1+n2
    s=n1-n2
    m=n1*n2
    d=n1/n2

    if calculadora:
        resultado=s
        
    elif calculadora:
        resultado=a

    elif calculadora:
        resultado=m

    elif calculadora:
        resultado=d 


    print(f"o resultado da operação é{resultado}")
        
        
    break




        





   

