# ordenar una lista de numeros ingresados por el usuario(bubble sort)
#Insrucciones:

#Solicita al usuario que ingrese 6 numeros separados por espacios
#Usa el mtodo de ordenacion burbuja para organizarlos de menor a mayor
#Muestre la lista ordenada

numeros=input("Ingrese 6 numeros separados por espacios: ").split()

for i in range(len(numeros)):
    numeros[i]=int(numeros[i])

n=len(numeros)
for i in range(n-1):
    for j in range(n-1-i):
        if numeros[j]>numeros[j+1]:
            numeros[j],numeros[j+1]=numeros[j+1],numeros[j]
print(f"La lista ordenada es: {numeros}") 