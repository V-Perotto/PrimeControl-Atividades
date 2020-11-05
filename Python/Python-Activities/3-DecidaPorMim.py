import random
import time

lista = []
cont = 5

for item in range(5):
    print("\nMe diga", cont,"coisas que você gosta")
    item = str(input(">> "))
    lista.append(item)
    cont = cont - 1

print("\nAgora eu vou escolher para você um desses itens!")
time.sleep(2)
print("\nEu escolhi", random.choice(lista))