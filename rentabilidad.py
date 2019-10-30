import os
os.system ("cls")
##adjuntarlo con tiempo :v
ganancia = 0
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
        print("El producto puede ser reemplazado por otro con menos precio de importe.")
    else:
        print("Es recomendable dejar de vender este producto y sus parecidos.")
else:
    print ("El producto no genera ganacia ni perdida.")

