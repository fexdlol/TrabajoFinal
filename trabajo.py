<<<<<<< HEAD

=======
import os
>>>>>>> 0f998eef31f116700c3cc30549578dd036fdedcc

os.system ("cls")

#Inicio
print("Este programa solo analizará un tipo de producto a la vez")
print("El IGV tiene valor de 18.0%")
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
ingr = float(input("Ingrese el ingreso del producto: "))
while True:
    if (ingr <= 0):
        ingr = float(input(("Ingrese una cantidad valida del ingreso: ")))
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