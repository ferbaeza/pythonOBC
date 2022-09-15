def first(year):
    if year % 4 != 0: 
        print("No es bisiesto")
    elif year % 4 == 0 and year % 100 != 0:
        print("Es bisiesto")
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: 
        print("No es bisiesto")
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        print("Es bisiesto")

if __name__ == '__main__':
    print('Ejercicio 5\n')

    year = int(input('Introduce el año que tu quieras: '))
    print('\nEl año que has seleccionado es {}. \n'.format(year))

    first(year)
