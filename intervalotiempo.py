import os
os.system("cls")

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
       

