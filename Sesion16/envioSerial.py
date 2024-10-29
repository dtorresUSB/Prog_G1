import serial
import time

def comunicar(dato):
    pos=30
    ser=serial.Serial('COM2',baudrate=9600,timeout=1)
    primer='\n'
    # ser.write(primer.encode('utf-8'))
    time.sleep(2)
    print('Conexion activa.......')
    print('enviado...')
    envio=f'{dato}\n'
    ser.write(envio.encode('utf-8'))
    time.sleep(0.8)
    try:
        while ser.in_waiting>0:
            line=ser.readline(ser.in_waiting).decode('ascii')
            print(line)
        return line.rstrip('\n')
    except:
        print('Error de lectura')
        return 'error'

if __name__=="__main__":
    ang=input('Dato de envio: ')
    comunicar(ang)