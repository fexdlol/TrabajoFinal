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
if (tiempo == "semanal"):
    inter = int(input("Ingrese intervalo de tiempo: "))
    while True:
        if (inter <= 0):
            inter = int(input(("Ingrese un intervalo de tiempo valido: ")))
        
        else:
            for inter in range (1,5):
                break
if (tiempo == "mensual"):
    inter = int(input("Ingrese intervalo de tiempo: "))
    while True:
        if (inter <= 0):
            inter = int(input(("Ingrese un intervalo de tiempo valido: ")))
        else:
            break

inter = int(input("Ingrese intervalo de tiempo: "))
while True:
    if (inter < 0):
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
ganancia = 0
ganancia = ingreso - costo

#IGV
IGV = precioventa * 0.18
IGV = round(IGV,2)
#total
total = IGV + precioventa
total = round(total,2)

print("IGV: ", IGV)
print ("Pago total es: ", total)

#Salida
if (ganancia>0):
    print("El producto genera una ganacia de: S/.",ganancia )
    if(ganancia>0 and ganancia<=10):
        print("El producto tiene una rentabilidad buena.")
    elif(ganancia>10 and ganancia<=30):
        print("El producto tiene una rentabilidad aceptable.")
    elif(ganancia>30 and ganancia<=50):
        print("El producto tiene una rentabilidad genial.")
    else:
        print("El producto tiene una rentabilidad excelente.")
elif (ganancia<0):
    print("El producto genera una perdida de: S/.", ganancia,)
    if(ganancia<0 and ganancia>=-30):
        print("Lo recomendable es subir el precio de venta.")
    elif(ganancia<-30 and ganancia>=-50):
        print("El producto puede ser reemplazado por otro con menos precio de importe o esperar más tiempo.")
    else:
        print("Es recomendable dejar de vender este producto y sus parecidos.")
else:
    print ("El producto no genera ganacia ni perdida.")

#Resumen

print("Nombre del producto: ",name)
print("Cantidad importada: ",cantidad)
print("Cantidad vendida: ",cantidadvend)  
print("Precio de importe por producto: ", precioimport)
print("Precio de venta por producto: ", precioventa)
print("Intervalo de tiempo: ",inter, " ",tiempo)
print("El IGV del 18% por cada producto: ",IGV)

