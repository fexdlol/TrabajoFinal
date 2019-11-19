import time
import os
os.system("cls")
import sys
import sqlite3
import getpass
 
#declaracion de variables
print("******Bienvenido al sistema de analisis de productos******")
usuarios = "admin"
contraseña = "1234"
 
#declaracion de funciones
def login(usuario,passw):
    if usuario in usuarios:
        if passw in contraseña:
            return 1
        else:
            print("\n\tLa contraseña no coincide >:v ...\n")
    else:
        return 2
 
 #inicializacion de procesos
while True: 
    usuario=input('Usuario: ')
    passw = getpass.getpass('Contraseña: ')
    if login(usuario,passw)==1:
        print('Bienvenido ',usuario)
        break
    else:
        print('ERROR! Usted no esta registrado >:v .')


#Inicio
print("*****Este programa solo analizará un tipo de producto a la vez******")
while True:
    archivo = open ("prueba1.csv" , "a")
    productos = []
    name = input("Ingrese el nombre del producto: ")
    productos.append(name)

    archivo.write(name +" \n" )
   

  

    precioventa = float(input("Ingrese precio de venta del producto: "))
    archivo.write('precio de venta= % s' %precioventa +" \n")
    while True:
        if (precioventa <= 0):
            precioventa = float(input(("Ingrese un precio de venta valido: ")))

        else: 
            break   
    productos.append(precioventa)
    



    #precioimport = es el precio real del producto cuando se importa
    precioimport = float(input("Ingrese precio fijo: "))
    archivo.write('precio fijo= % s' %precioimport +" \n")
    while True:
        if (precioimport <= 0):
            precioimport = float(input(("Ingrese un precio fijo valido: ")))
        else:
            break
    productos.append(precioimport)
    
    cantidad = int(input("Ingrese la cantidad del producto importado: "))
    archivo.write('Cantidad importado= % s' %cantidad +" \n")
    while True:
        if (cantidad <= 0):
            cantidad = int(input(("Ingrese una cantidad valida: ")))
        else:
            break
    productos.append(cantidad)

    cantidadvend = int(input("Ingrese la cantidad vendida: "))
    archivo.write('Cantidad Vendida= % s' %cantidadvend +" \n")
    while True:
        if (cantidadvend <= 0):
            cantidadvend = int(input(("Ingrese una cantidad valida de la venta: ")))
        else:
            break
    productos.append(cantidadvend)

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

    print ("Pago total es: ", total)

    #Salida
    if (ganancia>0):
        print("El producto genera una ganacia de: S/.",ganancia )
        print("\n************************** FELICICIDADES ***************************")
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
        print("\n************************** ACCIÓN RECOMENDADA ***************************")
        if(ganancia<0 and ganancia>=-30):
            print("Lo recomendable es subir el precio de venta.")
        elif(ganancia<-30 and ganancia>=-50):
            print("El producto puede ser reemplazado por otro con menos precio de importe o esperar más tiempo.")
        else:
            print("Es recomendable dejar de vender este producto y sus parecidos.")
    else:
        print("*****************************************************")
        print ("El producto no genera ganacia ni perdida.")
    
    asterisco = "**************"
    archivo.write(asterisco + "\n")
    #Resumen
    print("\n *************************** RESUMEN ***************************")  
    print("El producto es: ", productos[0], "\nPrecio de venta por producto: ", productos[1],"\nPrecio de importe por producto: ", productos[2] ,"\nCantidad importada: ", productos[3],"\nCantidad vendida: ",productos[4] )
    print("El IGV del 18% por cada producto: ",IGV)
    rpta = input("Desea ingresar otro podructo(SI/NO): ")
    
    if (rpta == "SI" or rpta == "si"):
        print ("Ingrese otro producto: ")
    elif (rpta == "NO" or rpta == "no"):
        break
        