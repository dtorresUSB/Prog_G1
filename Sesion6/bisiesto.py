
def bisiesto(x):
    if x%4==0:
        if x%100==0:
            if x%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def main():
    year=int(input('Cual es su edad: '))
    for i in range(2024-year,2025):
        n=bisiesto(i)
        if n:
            print(i,'....Si es bisiesto')
        else:
            print(i,'....No es bisiesto')

if __name__=="__main__":
    main()

