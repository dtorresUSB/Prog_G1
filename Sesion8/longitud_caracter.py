
def longitud(lista):
    #----------valores iniciales----------
    idx=0
    maximo=len(lista[0])
    valores=[]
    #-------------------------------------
    for i in lista:
        if len(i)>len(lista[idx]):
            idx=lista.index(i)
            maximo=len(i) 
            valores.clear()
            valores.append(i)
        elif len(i)==len(lista[idx]):
            valores.append(i)
    return valores  

def main():
    my_list = ["adele","david", "mark", "dorothy", "tim", "hedy", "richard"]
    valores=longitud(my_list)
    for i in valores:
        print(f'El elemento {i} tiene la mayor longitud con {len(i)} caracteres')


if __name__=="__main__":
    main()