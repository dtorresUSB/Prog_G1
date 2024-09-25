
class Ciudadano:
    def __init__(self,nombre:str,nation:str,edad:int):
        self.nombre=nombre
        self.nacionalidad=nation
        self.edad=edad

    def setNombre(self,nombre:str):
        self.nombre=nombre
    
    def setNacionalidad(self,nation:str):
        self.nacionalidad=nation

    def setEdad(self,edad:int):
        self.edad=edad

    def getNombre(self):
        return self.nombre
    
    def getNacionalidad(self):
        return self.nacionalidad
    
    def getEdad(self):
        return self.edad
    
    def saludo(self):
        return f'Hola soy Goku'

class Colombiano(Ciudadano):
    def __init__(self,nombre:str,nation:str,edad:int,cc:int):
        super().__init__(nombre,nation,edad)
        self.CC=cc
        self.frase='Veci como esta!'

    def setCC(self,cc:int):
        self.CC=cc

    def setFrase(self,frase:str):
        self.frase=frase

    def getCC(self):
        return self.CC
    
    def getFrase(self):
        return self.frase
    
    def saludo(self):
        return f'Hola soy {self.nombre}, {self.frase}'

class Ingles(Ciudadano):
    def __init__(self,nombre:str,nation:str,edad:int,id:int):
        super().__init__(nombre,nation,edad)
        self.ID=id
        self.phrase='How are you?'

    def setCID(self,id:int):
        self.ID=id

    def setPhrase(self,phrase:str):
        self.phrase=phrase

    def getID(self):
        return self.ID
    
    def getPhrase(self):
        return self.phrase
    
    def saludo(self):
        return f'Hello, my name is {self.nombre}, {self.phrase}'

class Chino(Ciudadano):
    def __init__(self,nombre:str,nation:str,edad:int,sfz:int):
        super().__init__(nombre,nation,edad)
        self.SFZ=sfz
        self.yu='Ni Hao ma?'

    def setSFZ(self,sfz:int):
        self.SFZ=sfz

    def setYu(self,yu:str):
        self.yu=yu

    def getSFZ(self):
        return self.SFZ
    
    def getYu(self):
        return self.yu
    
    def saludo(self):
        return f'Ni gan ma ya, {self.nombre}, {self.yu}'

def main():
    futbolista1=Colombiano('Radamel Falcao','Colombia',36,123124)
    futbolista2=Ingles('David Beckham','Inglaterra',49,23434)
    actor=Chino('Jackie Chan','Chino',70,4564)
    Goku=Ciudadano('Son Goku','Dragon Ball',37)

    print('1. Conocer a Radamel Falacao\n'
          '2. Conocer a David Beckham\n'
          '3. Conocer a Jackie Chan\n'
          '4. Conocer a Goku\n')
    
    opc=int(input('A quien quiere conocer!: '))

    personajes = [futbolista1,futbolista2,actor,Goku]

    persona=personajes[opc-1]
    print(f'Hola mi nombre es {persona.getNombre()}\n'
              f'Edad: {persona.getEdad()}\n'
              f'Nacionalidad: {persona.getNacionalidad()}\n\n'
              f'{persona.saludo()}')

if __name__=="__main__":
    main()