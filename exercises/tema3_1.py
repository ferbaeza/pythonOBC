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
    print(p)


if __name__ == '__main__':
    exercise_three()
