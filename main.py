print("Ejercicio 2 secuencia de Fibonacci")
num = int(input("Introduce la cantidad de números de la secuencia que deseas: "))
print("numeros de la secuencia :",num)
a=0
b=1
c=1
print("La secuencia es:")
while c<=num:
    if c==1:
        print(" ",a)
    elif c==2:
        print(" ",b)
    else:
        prox=a+b
        print(" ",prox)
        a=b
        b=prox
    c=c+1