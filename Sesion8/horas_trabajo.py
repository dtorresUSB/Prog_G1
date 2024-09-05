def horasTrabajo(x,y,z):
    rate=1
    if z=='Domingo':
        rate=2
    valor=x*y*rate
    return valor



if __name__=="__main__":
   vHora=int(input('Ingrese el valor de la hora: ')) 
   horaTrabajo=float(input('Ingrese el número de horas trabajadas: '))
   dia=input('Ingrese el nombre del día: ').capitalize()
   dinero=horasTrabajo(vHora,horaTrabajo,dia)
   print(f'El valor a pagar es: {dinero}')