class Alumno():
    def __init__(self, nombre, nota):
        self.nombre= nombre
        self.nota= nota

    def print(self):
        print(('El alumno {} tiene una nota de {}'.format(self.nombre, self.nota)))

    def result(self):
        if self.nota >= 5:
            print('El alumno {} ha aprobado'.format(self.nombre))
        elif self.nota <5:
            print('El alumno {} ha suspendido'.format(self.nombre))

alumno = Alumno('Fernando', 7)
alumno.print()
alumno.result()