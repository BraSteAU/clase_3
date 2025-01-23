#Ordenar lista de palabras alfabeticamente (Insertion sort)
#Instrucciones:

#Solicita al usuario que ingrese 5 palabras separadas por espacios
#Ordena las palabras en orden alfabetico utilizando el metodo de insercion
#Muestra la lista ordenada

palabras= input("Ingrese 5 palabras separadas por espacios ").split()

for i in range(1,len(palabras)):
    clave=palabras[i]
    j=i-1
    while j>=0 and clave<palabras[j]:
        palabras[j+1]=palabras[j]
        j-=1
    palabras[j+1]=clave
print(f"Palabras ordenadas alfabeticamente: {palabras}")