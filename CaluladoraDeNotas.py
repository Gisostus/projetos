#feito em 14/06/2025
while True:
 conceito = float(input("Digite sua nota "))

 conceitoA = 9
 conceitoAL = 'A'
 conceitoB = 7
 conceitoBL = 'B'
 conceitoC = 5
 conceitoCL = 'C'
 conceitoD = 3
 conceitoDL = 'D'
 conceitoF = 0
 conceitoFL = 'F'



 if conceito >= conceitoA:
    print(f"Conceito = {conceitoAL}")
 elif conceito >= conceitoB:
    print(f"Conceito = {conceitoBL}")
 elif conceito >= conceitoC:
    print(f"Conceito = {conceitoCL}")
 elif conceito >= conceitoD:
    print(f"Conceito = {conceitoDL}")
 elif conceito >= conceitoF:
    print(f"Conceito = {conceitoFL}")

 resposta = input("Deseja verificar outra nota? (s/n)").lower()
 if resposta != 's':
    print("Encerrando Programa ")
    break





