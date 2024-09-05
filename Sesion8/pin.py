from random import randint as r

def pin_secreto():#va a ayudar a completar de ceros a la izq el pin
    secret=str(r(0,9999))
    # if len(secret)!=4:      #3 => concatenar (+)
    #     for i in range(4-len(secret)):
    #         secret='0'+ secret      
    #     print(secret)
    while len(secret)<4:
        secret='0'+secret
    print(secret)
    return secret

def pin():
    secret=pin_secreto()
    password=input('Ingrese el pin: ')
    contador=1
    while password!=secret:
        print('Lo siento, pin erroneo')
        password=input('Ingrese el pin: ')
        contador+=1
        if contador==5:
            print(f'Pista: {secret}')
    if contador==1:
        print(f'Lo lograste en {contador} intento')
    else:
        print(f'Lo lograste en {contador} intentos')



if __name__=="__main__":
    pin()