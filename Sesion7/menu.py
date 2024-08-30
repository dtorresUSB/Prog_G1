def agregar(lista):
    dato=int(input('Ingrese un valor en la lista: '))
    lista.append(dato)
    return lista

def insertar(lista):
    idx=int(input('Ingrese un indice: '))
    val=int(input('Ingrese un valor: '))
    lista.insert(idx,val)
    return lista

def formatear(lista):
    lista.clear()
    return lista

def remover(lista):
    x=int(input('Qué valor desea remover: '))
    lista.remove(x)
    return lista

def main():
    lista=[83,29,10]
    while 1:
        print('\nMétodos de las listas\n'
            'Seleccione una de las siguientes opciones:\n'
            '1. Agregar un elemento a la lista\n'
            '2. Agregar un elemento en el indice especifico\n'
            '3. Borrar la lista completamente\n'
            '4. Quitar un dato de la lista\n')
        
        opc=int(input('Ingrese una opción:'))

        menu=[agregar,insertar,formatear,remover]
        lista=menu[(opc-1)](lista)
        
        print(f'lista =>{lista}\n')


if __name__=="__main__":
    main()