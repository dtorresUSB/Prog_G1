#Para ejecutar cualquiera de los codigos, recuerde quitar el comentario al inicio de 
#la linea de código.

#------------------Conocer el tipo de variable------------------
x=5
print(type(x))
#------------------Solicitar datos a un usuario------------------
x=int(input('Ingrese un numero: '))
y=x+2
print(y)
#-------------------------Comentarios----------------------------
#para comentar un codigo se debe utilizar el simbolo "#" al inicio
#de la linea.
#puede utilizar los comandos "ctrl+k" seguido de "ctrl+c" para comentar
#puede utilizar los comandos "ctrl+k" seguido de "ctrl+u" para quitar
#el comentario.
#tambien puede utilizar """ al inicio y """ al final

#------------Programa identificar numeros pares e impares--------
x=int(input('Ingrese un numero: '))
if x%2==0:
    print('El numero es PAR')
else:
    print('El numero es IMPAR')
#-------------------Programa area de un circulo--------------------
pi=3.14
r=float(input('Ingrese el valor del radio: '))
A=pi*r**2
print('El area es',A)