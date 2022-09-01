def exercise_three():
    print('Rellena los campos solicitados')
    name= input('Introduzca su nombre : ')
    surname= input('Introduzca sus apellidos : ')
    age= input('Introduzca su edad : ')
    email= input('Introduzca su email : ')
    phone= input('Introduzca su telefono : ')
    friends=[]
    friends.append(input('Dime el nombre de dos amigos: '))
    favourites_films={}
    p=favourites_films['peliculas_vistas'] = input('Dime el nombre de las peliculas que has visto: ')

    print('\nLos datos introducidos son : \n\n {} {} de {} anyos de edad \n email: {} \n phone: {}\n\n'.format(name, surname, age, email, phone))
    print('Nombre de tus amigos: ')
    for friend in friends:
        print(friend)

    print('\nNombre de las peliculas vistas: ')
    print(p,'\n')

    
def exercise_three_two():
    a=5.1
    b=a**2
    print(b)
    print('\nIntroduce tu peso en Kg:  ... por ejemplo 76,8 Kg')
    print('\nIntroduce tu altuta en metros :  ... por ejemplo 1,76 m\n')
    peso = float(input('Introduce tu peso: '))
    altura = float(input('Introduce tu altura: '))
    imc = float(peso/altura**2)
    imc = "{0:.2f}".format(imc)
    print('\nLos datos introducidos son: {} kg y una altura de {} m nTu IMC es de {}'.format(peso, altura, imc))

if __name__ == '__main__':
    exercise_three()
    exercise_three_two()
