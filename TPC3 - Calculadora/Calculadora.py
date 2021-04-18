print("Bem vindo à melhor calculadora de sempre.")
print("Por favor insere o primeiro número, a operação a realizar, e depois o segundo número.")
print("Sou capaz de fazer somas (+), subtrações (-), multiplicações (*) e divisões (/)")

#input de variaveis
num1 = float(input("Primeiro número: "))
sinal = input("Operação matemática (+, -, *, /): ")
num2 = float(input("Segundo número: "))

#operações matematicas
if sinal == "+":
    num3 = num1 + num2
    print(str(num1) + " + " + str(num2) + " = " + str(num3))
elif sinal == "-":
    num3 = num1 - num2
    print(str(num1) + " - " + str(num2) + " = " + str(num3))
elif sinal == "*":
    num3 = num1 * num2
    print(str(num1) + " x " + str(num2) + " = " + str(num3))
elif sinal == "/":
    num3 = num1 / num2
    print(str(num1) + " / " + str(num2) + " = " + str(num3))
else:
    print("Não escolheste nenhum operador permitido")