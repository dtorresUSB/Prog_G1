class Materia :
    def __init__(self):
        self.nombre = None
        self.creditos = None
        self.profesor = None
        self.horario = None
        self.salon = None
    
    def txtHorario(self):
        txt = (f'La materia {self.nombre} que tiene {self.creditos} '
               f'creditos, a cargo del profesor {self.profesor} '
               f'en el horario de {self.horario} '
               f'en el salón {self.salon}')
        return txt

# def imprimir(materia):
#     print(f'La materia tiene {materia.creditos} créditos,\n'
#           f'a cargo del profesor {materia.profesor},\n'
#           f'en el horario de {materia.horario},\n'
#           f'en el salón {materia.salon}.')

def main ():
    mat=[['electricidad','3','Julian Ortiz','9 a 11 (martes y jueves)','303PS'],
         ['programacion','3','David Torres','11 a 1 (martes y jueves)','204GO']]

    obj_materia=[]    #obj_materia=[obj_elec, obj_pro]
    for i in range(2):
        obj_materia.append(Materia())
        obj_materia[i].nombre=mat[i][0]
        obj_materia[i].creditos=mat[i][1]
        obj_materia[i].profesor=mat[i][2]
        obj_materia[i].horario=mat[i][3]
        obj_materia[i].salon=mat[i][4]

    circuitos = Materia()
    circuitos.nombre = 'circuitos'
    circuitos.creditos = '3'
    circuitos.profesor = 'Roberto Bohorquez'
    circuitos.horario = '9 a 11 (miercoles y viernes)'
    circuitos.salon = '407DB'

    estatica = Materia()
    estatica.nombre = 'estatica'
    estatica.creditos = '3'
    estatica.profesor = 'Eliana Zuluaga'
    estatica.horario = '11 a 1 (miercoles y viernes)'
    estatica.salon = '206PS'

    multivariado = Materia()
    multivariado.nombre = 'multivariado'
    multivariado.creditos = '3'
    multivariado.profesor = 'Wilson Castro'
    multivariado.horario = '1 a 3 (miercoles y viernes)'
    multivariado.salon = '407DB'

    while 1:
        materia_elegida = input('¿Qué materia quieres revisar? (electricidad, programacion, \n'
                        'circuitos, estatica, multivariado): ').lower()
        if materia_elegida == 'electricidad':
            print(obj_materia[0].txtHorario())
            #imprimir(electricidad)
        elif materia_elegida == 'programacion':
            print(obj_materia[1].txtHorario())
            #imprimir(programacion)
        elif materia_elegida == 'circuitos':
            print(circuitos.txtHorario())
            #imprimir(circuitos)
        elif materia_elegida == 'estatica':
            print(estatica.txtHorario())
            #imprimir(estatica)
        elif materia_elegida == 'multivariado':
            print(multivariado.txtHorario)
            #imprimir(multivariado)
        else:
            print('materia incorrecta intenta de nuevo')
    
if __name__=='__main__':
    main()