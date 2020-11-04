import random
import math

def chuteNumero():
    num = math.ceil(10 * random.random())
    return num

var = int(input("Insira um número de 0 a 10: "))
chuteNumero = chuteNumero()

if chuteNumero == var:
    print("Seu número: \t\t[", var, "]")
    print("Número aleatório: \t[", chuteNumero, "]")
    print("Você acertou!")
else:
    print("Seu número: \t\t[", var, "]")
    print("Número aleatório: \t[", chuteNumero, "]")
    print("Você errou!")