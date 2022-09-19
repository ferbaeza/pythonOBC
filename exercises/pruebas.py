from functools import reduce
# #** Uso de Filter
# Extrae los valores que den True como resultado de la funcion
numeros =[1,2,3,4,5,6,7,8,9]
print(numeros)

alumnos = ["Alex", "Barth", "Carlos", "Baguira","Neon"]

def num_par(x):
    if x %2 ==0:
        return True
    return False

def name_start_b(x):
    if str(x).startswith("Ba"):
        return True
    return False

names_filtered = filter(name_start_b, alumnos)
print(list(names_filtered))

res = filter(num_par, numeros)
print(list(res))

#** Uso de MAP
# Map aplica la funcion a todos los elementos de la lista

def suma(x):
    return x+x

res_suma= map(suma, numeros)
print(list(res_suma))

#** Reduce
#Reduce va haciendo las opercaiones e iterando el resultado como valor de la funcion
#Al imprimir podemos ver  como el resultado de la primera iteracion, será a en la 2 iteracion
print(numeros)
def suma_reduce(a,b):
    print(f"a={a} +b={b} res= {a+b}")
    return a+b

red = reduce(suma_reduce, numeros)
print(red)


