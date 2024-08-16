#Para ejecutar cualquiera de los codigos, recuerde quitar el comentario al inicio de 
#la linea de código.

#-----------------Condicional Simple----------------
# txt=input('Ingrese un número: ')
# if txt>=10:
#     print('El número ingresado es mayor o igual a 10')
# else:
#     print('El número ingresado es menor a 10')

#-----------------Condicional Anidado---------------
# txt=input('Ingrese un día de la semana: ')
# if txt=='1':
#     print('Este día es Lunes')
# elif txt=='2':
#     print('Este día es Martes')
# elif txt=='3':
#     print('Este día es Miercoles')
# elif txt=='4':
#     print('Este día es Jueves')
# elif txt=='5':
#     print('Este día es Viernes')
# elif txt=='6':
#     print('Este día es Sabado')
# elif txt=='7':
#     print('Este día es Domingo')
# else:
#     print('Entrada Invalida, ingrese un número entre 1 y 7')

#--------------------Ejemplo 1-------------------------
# nota=float(input('Ingrese la nota del curso: '))
# if 3<=nota<5:
#     print('Aprobó')
# elif 0<nota<3:
#     print('Reprobó')
# else:
#     print('Entrada Invalida, la nota tiene un valor entre 0 y 5')

#--------------------Ejemplo 2-------------------------
a=int(input('Ingrese el valor de a: '))
b=int(input('Ingrese el valor de a: '))
c=int(input('Ingrese el valor de a: '))
raiz=b**2-4*a*c
if raiz>=0:
    print('La solución es real')
else:
    print('La solución es imaginaria')