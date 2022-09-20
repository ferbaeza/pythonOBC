import sqlite3
import pprint
def main():
    name = str(input("Selecciona el nombre del alumno que deseas buscar: "))
    conn =sqlite3.connect('app.db')
    cursor = conn.cursor()
    #pprint.pprint(dir(conn))

    rows = cursor.execute("SELECT * FROM alumnos ")
    lista=[]
    for row in rows:
        lista.append(row)

    for i in lista:
        if i[1]==name:
            print(f"Has encontrado al alumno que buscabas {name}")
    cursor.close()
    conn.close()


if __name__=="__main__":
    main()