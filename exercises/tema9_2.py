from functools import reduce
import random
random_list= []

for i in range(19):
    a=random.randint(3,200)
    random_list.append(a)
    i = i+1

print(f"Esta es una lista random {random_list}")

def num_impar(x):
    if x % 2 != 0:
        return True
    return False


res = filter(num_impar, random_list)
print("Estos son solo los numeros impares")
print(list(res))


def suma_reduce(a,b):
    return a+b

reduce_resultado = reduce(suma_reduce, random_list)
print(f"Y la suma de todos ells es= {reduce_resultado}")


