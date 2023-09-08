
import time #libreria para el tiempo

print("****************** CALCULADORA *******************")

print(" 1)...............  suma  ")
print(" 2)...............  resta  ")
print(" 3)............... multiplicacion  ")
print(" 4)...............  divison  ")
valor=int(input("escoja una opcion: "))
while valor != 5:
    if valor ==1: 
        numero1=int(input("introduzca el primer numero: "))
        numero2=int(input(" introduzca el segundo numero: "))
        inicio= time.time()
        print("el resultado es: ",numero1+numero2)
        fin= time.time()
        tiempo_ejecutado = fin-inicio
        print(tiempo_ejecutado)

    if valor ==2:
        numero1=int(input("introduzca el primer numero: "))
        numero2=int(input(" introduzca el segundo numero: "))
        inicio= time.time()
        print("el resultado es: ",numero1-numero2)
        fin= time.time()
        tiempo_ejecutado = fin-inicio
        print(tiempo_ejecutado)
        break;
    if valor ==3:
        numero1=int(input("introduzca el primer numero: ")) 
        numero2=int(input(" introduzca el segundo numero: "))
        inicio= time.time()
        print("el resultado es: ",numero1*numero2)
        fin= time.time()
        tiempo_ejecutado = fin-inicio
        print(tiempo_ejecutado)
        break;
    if valor ==4:
        numero1=int(input("introduzca el primer numero: "))
        numero2=int(input(" introduzca el segundo numero: "))
        inicio= time.time()
        print("el resultado es: ",numero1/numero2)
        fin= time.time()
        tiempo_ejecutado = fin-inicio
        print(tiempo_ejecutado)
        break;
       