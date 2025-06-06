nome_produto=input("nome do produto:")
valor_unitario=float(input("valor unitario:"))
quantidade=int(input("a quantidade comprada:"))
percentual_desconto=float(input("percentual de desconto:"))

valor_sem_desconto= valor_unitario * quantidade

desconto= valor_sem_desconto * (percentual_desconto)




valor_com_desconto= valor_sem_desconto - desconto

print(f"produto:{nome_produto}")
print(f"total da venda:R${valor_com_desconto:.2f}")