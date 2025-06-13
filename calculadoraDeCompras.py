print("=== CALCULADORA DE COMPRAS ===")
print("")
# Produto 1
nome_produto1 = input("Nome do produto 1: ")
preco_produto1 = float(input("Preço do produto 1: "))

# Produto 2
nome_produto2 = input("Nome do produto 2: ")
preco_produto2 = float(input("Preço do produto 2: "))

# Produto 3
nome_produto3 = input("Nome do produto 3: ")
preco_produto3 = float(input("Preço do produto 3: "))

print("=== NOTA FISCAL ===")

print(f"{nome_produto1} custou {preco_produto1}")
print(f"{nome_produto2} custou {preco_produto2}")
print(f"{nome_produto3} custou {preco_produto3}")

ValorTotal = (preco_produto1 + preco_produto2 + preco_produto3)

print(f"o total ficou {ValorTotal}")

if ValorTotal > 100:
     print("compra cara!")
else :print("compra barata!")




