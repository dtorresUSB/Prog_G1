
def minutos(min):
    sec=min*60
    return sec   #retorno de la salida

if __name__=="__main__":
    min=int(input('Ingrese los minutos a convertir en segundos: '))
    print(f'{minutos(min)} segundos')
