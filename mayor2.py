x=0
d=0
l=0
for n in range (0,10):
    n=int(input("Digite un numero entero"))
    if n>0:
        x+=1
    elif n==0:
        d+=1
    elif n<0:
        l+=1
print(x,"Positivos",d,"Iguales a cero",l,"Negativos")
