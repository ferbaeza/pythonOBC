def main():
    print("Tema9 ej_1")
    print("\nNecesitaremos tu ayuda\nNecesitamos crear una lista de paises\n")
    items=int(input("Introduce cuantos paises quieres tener en tu lista: "))
    print(items)
    
    countries= []
    i=0
    print("Introduce el nombre del pais :\n")
    while(int(i) < int(items)):
        inn=input("")  
        countries.append(inn)
        i = i+1

    c=[*set(countries)]
    list_two=[ x for x in c]
    countries_ordered= sorted(list_two)
    print("Los paises introducidos son: ")
    print(countries_ordered)
    


if __name__=="__main__":
    main()