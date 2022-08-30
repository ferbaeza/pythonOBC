def exercise_three():
    print('Rellena los campos solicitados')
    name= input('Introduzca su nombre : ')
    surname= input('Introduzca sus apellidos : ')
    age= input('Introduzca su edad : ')
    email= input('Introduzca su email : ')
    phone= input('Introduzca su telefono : ')

    print('\nLos datos introducidos son : \n\n {} {} de {} anyos de edad \n email: {} \n phone: {}\n\n'.format(name, surname, age, email, phone))


if __name__ == '__main__':
    exercise_three()
