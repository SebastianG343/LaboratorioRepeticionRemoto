n=""
x=0
n=int(input("Digite un numero"))
while n%2==0:
    n=int(input("Digite un numero"))
    x+=1
    if n%2!=0:
        print(x,"Numeros pares")