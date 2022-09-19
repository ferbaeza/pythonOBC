import os
from dataclasses import dataclass

def first():
    print('Ejercicio 2 Tema 8')

    @dataclass
    class Vehicle():
        name: str
        branch: str

        def __str__(self) -> str:
            return f'Your vehicle is {self.name} from {self.branch}'

    v1= Vehicle('beta','alfa')
    print(v1)
    print('Representacion del Objeto : '+repr(v1))

    
    ruta = '/home/fer/visual/openBootCamp/python/pythonOBC/exercises/'
    file = open(ruta+'Class.txt', 'w')
    file.write('Fernando Baeza\n'+ os.linesep) #Salto de linea
    file.write('Esta es la linea guardada de nuestro Objeto:'+ os.linesep) #Salto de linea
    file.write(repr(v1))
    file.close()
    # Creo un variable distinta solo para leerlo
    object = open(ruta+'Class.txt', 'r')
    print(object.read())
    object.close()



if __name__ == '__main__':
    first()
