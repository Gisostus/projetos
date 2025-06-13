operador = input("insira um sinal (+ - * / ** %) " )
numero1 = float(input("insira o primeiro numero " ))
numero2 = float(input("insira o segundo numero " ))

if operador == "+":
    resultado = numero1 + numero2
 #soma

if operador == "-":
     resultado = numero1 - numero2
 #menos

if operador == "*":
     resultado = numero1 * numero2
 #multiplicacao

if operador == "/":
     resultado = numero1 / numero2
 #divisao

if operador == "**":
      resultado = numero1 ** numero2
 #elevado

if operador == "%":
      resultado = numero1 % numero2
 #resto

print(resultado)

