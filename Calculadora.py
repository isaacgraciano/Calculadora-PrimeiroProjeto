print("Oi, eu sou sua calculadora!")

numero1 = float(input("Me da um numero: "))
numero2 = float(input("Segundo numero: "))

operacao = input("Qual operaçao? (soma, subtração, multiplicação, divisão): ")

if operacao == "soma":
    resultado = numero1 + numero2

elif operacao == "subtração":
    resultado = numero1 - numero2

elif operacao == "multiplicação":
    resultado = numero1 * numero2

elif operacao == "divisão":
    resultado = numero1 / numero2

    if numero1 == 0 or numero2 == 0:
        print("Não é possível dividir por zero.")
        exit()





print("A soma é: ", round(resultado, 2))


