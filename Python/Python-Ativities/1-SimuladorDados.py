import random
import math

def rolarDQuatro():
    num = math.ceil(4 * random.random())
    return num

def rolarDSeis():
    num = math.ceil(6 * random.random())
    return num

def rolarDOito():
    num = math.ceil(8 * random.random())
    return num

def rolarDDez():
    num = math.ceil(10 * random.random())
    return num

def rolarDVinte():
    num = math.ceil(20 * random.random())
    return num

d_quatro = rolarDQuatro()
print("Rolando um D4: ", d_quatro)

d_seis = rolarDSeis()
print("Rolando um D6: ", d_seis)

d_oito = rolarDOito()
print("Rolando um D8: ", d_oito)

d_dez = rolarDDez()
print("Rolando um D10: ", d_dez)

d_vinte = rolarDVinte()
print("Rolando um D20: ", d_vinte)