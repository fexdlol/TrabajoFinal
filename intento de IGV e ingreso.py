import os 
os.system("cls")


#precio
precio = float(input("Ingrese el precio del producto: "))
while True:
    if (precio <= 0):
        precio = float(input("Ingrese un precio valido: "))
    else:
        break
#IGV
IGV = precio * 0.18
round(IGV,1)
print("IGV: ", IGV)
#total
total = IGV + precio
round(total,1)
print ("Pago total es: ", total)