#Complejidad algoritmica y metodos de ordenacion
#(Bubble sort e insertion sort)

#La complejidad algoritmica mide los recursos que necesita un algoritmo para ejecutarse, y se mide en terminos de:

#Tiempo de ejecucion
   # cuanto tiempo toma ejecutar el agoritmo en funcion de la cantidad de los datos de entrada (n), se suele
   #expresar en big o o(n), o(n2), o(log n)

#Uso de memoria o complejidad espacial:   
#  cuanta memoria adicional requiere e algoritmo para ejecutarse, tambien se expresa en Big O

#Notacion Big O
#  describir como crece el tiempo de ejecucucion de un algoritmo en erelacion a su tamaño de entrada

#Como ordenar

#Es el proceso de organizar elementos en un orden especifico( ascendente y descendente)

#Ordenacion por burbuja o bubble sort
#   Compara elementos adyacentes y los intercambia si estan en orde incorrecto, se repite hasta que no se necesiten mas intercambios


numeros=[5,3,8,4,2]#n=len(numeros)
n=len(numeros)
for i in range(n-1):
   for j in range(n-1-i):
        if numeros[j]>numeros[j+1]:
            temp = numeros[j]
            numeros[j]=numeros[j+1]
            numeros[j+1]=temp
print(f"Lista ordenada con bubble sort: {numeros}")


#Metodo de ordenacion por insercion sort
#  Construye una lista ordenada de manera incremental, insertando cada elemento en la posicion correcta respecto a los ya ordenados

num=[7,3,5,2,6]
n=len(num)

for i in range(1,n):
    clave=num[i]
    j=i-1
    while j>=0 and num[j]>clave:
        num[j+1]=num[j]
        j-=1
    num[j+1]=clave
print(f"Lista ordenada con insertion. {num}") 

