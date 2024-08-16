#Para ejecutar cualquiera de los codigos, recuerde quitar el comentario al inicio de 
#la linea de código.

#----------------While-------------------
# x=0
# while x<10:
#     x+=1
#     print(x)

#-----------Uso del break----------------
# x=0
# while x<10:
#     x+=1
#     if x==4:
#         break
#     print(x)

#-------------Uso del continue----------
# x=0
# while x<10:
#     x+=1
#     if x==4:
#         continue
#     print(x)

#-------------- Uso del pass -----------
# x=0
# while x<10:
#     pass

#------------- Bucle infinito------------
# txt=''
# while txt!='salir':
#     txt=input('Ingrese una palabra: ')
#     print(txt)


# while 1:    #while True:
#     txt=input('Ingrese una palabra: ')
#     if txt=='salir':
#         break
#     print(txt)

# x=0       #Ojo el orden de las lineas de codigo SI IMPORTA "Ctrl+c" para terminar el programa
# while x<10:
#     print(x)
#     if x==4:
#         continue
#     x+=1

#---------------Uso del for--------------
# for i in range(1,10,2):
#     print(i)

#----------------Ejemplo 1---------------
# x=0
# for i in range(10):
#     x+=0.1
#     #print(round(x,2))
#     print(f'{x:.3f}')

# for i in range(1,11):
#     print(i/10)

#--------------- Ejemplo2----------------
# year=int(input('Cual es su edad: '))
# print('Años vividos')
# for i in range(2024-year,2024):
#     print(i)

#----------------Ejemplo3----------------
n=int(input('Hasta que numero desea generar los números impares: '))
i=1;impar=1
while impar<=n:
    print(impar)
    impar=2*i+1
    i+=1
