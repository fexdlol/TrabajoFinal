import os
os.system("cls")

cantidadvendida = int(input("Ingrese la cantidad vendida: "))
precioproducto = float(input("Ingrese precio del producto: "))
fijo = float(input("Ingrese precio fijo: "))
a = 0

while True:
    if (cantidadvendida <= 0):
        cantidadvendida = int(input("Ingrese cantidad valida: "))
    else:
        break
while True:
    if (precioproducto <= 0):
        precioproducto = float(input("Ingrese precio valido: "))
    else:
        break
while True:
    if (fijo <= 0):
        fijo = float(input("Ingrese precio fijo valido: "))
    else:
        break

ing = 0
ing = cantidadvendida * precioproducto
costo = fijo + precioproducto
Ganancia = 0
Ganancia = ing - costo

print(Ganancia)