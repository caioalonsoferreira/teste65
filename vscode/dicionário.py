

'''
conta={}


conta['num']=int(input("digite o numero:"))
conta['saldo']=float(input("digite o numero:"))
conta['nome']=input("digite o numero:")

print(conta)
'''








user=input("digite uma frase")

palavras=user.split()

contagem_palavras={}

for palavra in palavras:
        if palavra in contagem_palavras:
                
            contagem_palavras[palavra]+=1

        else:
               
               contagem_palavras[palavra]=1




for palavra,contagem in contagem_palavras.items():
        print(f"{palavra}:{contagem}")
                


