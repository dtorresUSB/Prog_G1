import math

def main():
    x=float(input('Ingrese la coordenada en x: '))
    y=float(input('Ingrese la coordenada en y: '))

    r=math.sqrt(x**2+y**2)

    if r<=1:
        print('Anotó 10 punto')
    elif r<=5:
        print('Anotó 5 puntos')
    elif r<=10:
        print('Anotó 1 punto')
    else:
        print('No anotó ningun punto')

def busqueda():
    lista=[8,35,6,4,5,3,9]
    lista.sort()
    num=int(input('Ingrese el valor de busqueda: ')) #35 

    while 1:
        lenght=len(lista)  #[35]
        mitad=lenght//2

        if lista==[]:
            print('No se encuentra el dato en la lista')
            break
        if num==lista[mitad]:
            print('felicidades el numero esta en la lista')
            break
        elif num>lista[mitad]:
            for i in range(0,mitad+1):
                lista.pop(0)
            print(lista)
        elif num<lista[mitad]:
            for i in range(mitad,lenght):
                lista.pop(-1)
            print(lista)
        


if __name__=="__main__":
    opc=input('Ingrese la opcion: ')
    if opc=='1':
        main()
    elif opc=='2':
        busqueda()
