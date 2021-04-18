import random

secret = random.randint(0, 20)

numUser = int(input("Escolhe um número de 0 a 20"))

if secret == numUser:
    print("Parabens! Acertaste! o número era o " + str(secret))
else:
    print("Não acertaste desta vez... O numero certo era o " + str(secret))