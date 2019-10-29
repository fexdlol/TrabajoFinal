# NETO = TOTAL/(1+0.18)
# IGV = TOTAL - NETO
import os

os.system ("cls")

#Inicio
print("Este programa solo analizará un tipo de producto a la vez")

name = input("Ingrese el nombre del producto: ")
inter = int(input("Ingrese intervalo de tiempo: "))
while True:
    if (inter <= 0):
        inter = int(input(("Ingrese un intervalo de tiempo valido: ")))
    else:
        break
#Cantidad = can
can = int(input("Ingrese la cantidad del producto importado: "))
while True:
    if (can <= 0):
        can = int(input(("Ingrese una cantidad valida: ")))
    else:
        break
ingr = int(input("Ingrese el ingreso del producto: "))
while True:
    if (ingr <= 0):
        ingr = int(input(("Ingrese una cantidad valida del ingreso: ")))
    else:
        break
vend = int(input("Ingrese la cantidad vendida: "))
while True:
    if (vend <= 0):
        vend = int(input(("Ingrese una cantidad valida de la venta: ")))
    else:
        break


#Proceso



#Salida