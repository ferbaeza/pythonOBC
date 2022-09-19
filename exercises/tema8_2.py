import os
from dataclasses import dataclass
import pickle

#Version 1 with serialized Data
class Coche():
    name="",
    branch=""

    def __init__(self, name, branch) -> None:
        self.name=name,
        self.branch=branch

    def get_full_name(self):
        return f"Your car is a {self.branch} {self.name}"


#Version 2 with NO-serialized Data
@dataclass
class Vehicle():
    name: str
    branch: str

    def __str__(self) -> str:
        return f'Your vehicle is {self.name} from {self.branch}'

ruta = '/home/fer/visual/openBootCamp/python/pythonOBC/exercises/'

#Using picke to serialized data
coche= Coche('Ibiza','Seat')
f= open(ruta+"Class.bin", "wb")
pickle.dump(coche, f)
f.close()

#Objet2 
v1=Vehicle("beta", "alfa")
print(v1)
print('Representacion del Objeto : '+repr(v1))
#Saved Ob2 in txt
file = open(ruta+'Class.txt', 'w')
file.write('Fernando Baeza\n'+ os.linesep) #Salto de linea
file.write('Esta es la linea guardada de nuestro Objeto:'+ os.linesep) #Salto de linea
file.write(repr(v1)) 
file.close()



#Get the data from the binary Text with pickle
old= open(ruta+"Class.bin", "rb")
old_car= pickle.load(old)
old.close()

print(type(old_car))
print(repr(old_car))
print(old_car.get_full_name())