
def fibonacci(n):
    
    x=0
    y=1 #estos son los primeros terminos de la serie
    if numero == 0:
        return x
    elif numero == 1:
        return y
    
    for _ in range(2, numero + 1):
         x, y = y, x + y
    return y
numero = int(input("Ingrese la posición numero para obtener el término de la serie de Fibonacci: "))
resultado = fibonacci(numero)
print("El término en la posición ",numero,"de la serie de Fibonacci es:",resultado)
