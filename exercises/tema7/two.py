import time as t
def seven_two():
    local_time = t.ctime()
    #print (hora)
    named_tuple = t.localtime() # get struct_time
    time_string = t.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    hora = t.strftime("%H", named_tuple)
    minutes = t.strftime("%M", named_tuple)
    print(f'Son las {hora}:{minutes} h')

    if int(hora) >= 19:
        print(f'Es ya tarde, son las {hora}h')
    else:
        res_horas = int(hora)-24
        res_minutess = int(minutes)-59
        if res_horas<1:
            print(f'Quedan {res_minutess} minutos para acabar')
        else:
            print(f'Quedan {res_horas}:{res_minutess}h para acabar')




    print (str(local_time))



if __name__ == '__main__':
    seven_two()