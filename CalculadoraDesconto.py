while True:
    try:
        valor: float = float(input("qual o valor da compra? "))
        break
    except:
        print("erro, digite o valor em X.0")

if valor <= 100:
    desconto = 0
elif valor <= 200:
    desconto = 0.05
elif valor <= 500:
    desconto = 0.1
else:
    desconto = 0.15

DescontoUsuario = desconto
ValorFinal = valor * desconto

print(f"o desconto sera de {DescontoUsuario * 100}%!")
print(f"o valor final sera de {valor - ValorFinal}")
# feito para um desafio com o ChatGPT em 16/06/2025

