from random import randint as r

def matriz(filas,columnas):
    matrix=[]
    for i in range(filas):
        matrix.append([])
        for j in range(columnas):
            #txt=f'Ingrese un numero [{i}][{j}]: '
            #um=int(input(txt))
            num=r(0,20)
            matrix[i].append(num)
    
    for i in matrix:
        print(i)

    escalar=int(input('Ingrese el numero escalar: '))

    #crear el algoritmo que recorra la matriz y la multiplique
    #termino a termino por el escalar


def main():
    filas=int(input('Ingrese el numero de filas: '))
    columnas=int(input('Ingrese el numero de columnas: '))
    matriz(filas,columnas)


if __name__=="__main__":
    main()