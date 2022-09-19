import os
def first():
    print('Ejercicio 1 Tema 8')
    ruta = '/home/fer/visual/openBootCamp/python/pythonOBC/exercises/'
    file = open(ruta+'testq.txt', 'w')
    file.write('Fernando Baeza'+ os.linesep)
    file.write('Hello from OpenBootCamp')
    file.close()



if __name__ == '__main__':
    first()
