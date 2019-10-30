import os
os.system ("cls")

#Inicio
print("Este programa solo analizará un tipo de producto a la vez")

name = input("Ingrese el nombre del producto: ")

precioventa = float(input("Ingrese precio de venta del producto: "))
while True:
    if (precioventa <= 0):
        precioventa = float(input(("Ingrese un precio de venta valido: ")))
    else:
        break

#precioimport = es el precio real del producto cuando se importa
precioimport = float(input("Ingrese precio fijo: "))
while True:
    if (precioimport <= 0):
        precioimport = float(input(("Ingrese un precio fijo valido: ")))
    else:
        break

tiempo = input("¿Que intervalo de tiempo quiere eleguir?(semanal/mensual): ")
while True:
    if (tiempo == "semanal"):
        print("Eliguío la opcion semanal")
        break
    if (tiempo == "mensual"):
        print("Eliguío la opcion mensual")
        break
    else:
        tiempo = input("Ingrese una opcion valida (semanal/mensual):")

inter = int(input("Ingrese intervalo de tiempo: "))
while True:
    if (inter <= 0):
        inter = int(input(("Ingrese un intervalo de tiempo valido: ")))
    else:
        break


cantidad = int(input("Ingrese la cantidad del producto importado: "))
while True:
    if (cantidad <= 0):
        cantidad = int(input(("Ingrese una cantidad valida: ")))
    else:
        break

cantidadvend = int(input("Ingrese la cantidad vendida: "))
while True:
    if (cantidadvend <= 0):
        cantidadvend = int(input(("Ingrese una cantidad valida de la venta: ")))
    else:
        break

print("RECUERDE: El IGV tiene valor de 18.0% por el precio del producto")
#Proceso
ingreso = 0
ingreso = cantidadvend * precioventa
costo = cantidad * precioimport
Ganancia = 0
Ganancia = ingreso - costo

#IGV
IGV = precioventa * 0.18
IGV = round(IGV,2)
#total
total = IGV + precioventa
total = round(total,2)

print("IGV: ", IGV)
print ("Pago total es: ", total)
print(Ganancia)


#Salida
