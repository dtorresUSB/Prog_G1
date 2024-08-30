from ProgG2.Sesion5.factorial import n_factorial as f

def main():
    equipos=int(input('Ingrese el numero de equipos: '))
    grupos=int(input('Ingrese el numero de grupos: '))
    x=f(equipos)/(f(grupos)*f(equipos-grupos))
    print(f'La combinación de {equipos} equipos de a {grupos} grupos es: {x}')


if __name__=="__main__":
    main()