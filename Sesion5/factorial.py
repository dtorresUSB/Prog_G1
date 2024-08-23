
def n_factorial(x):
    n=1
    for i in range(x):
        n*=(i+1)
    return n

if __name__=="__main__":
    res=n_factorial(5)
    print(res)