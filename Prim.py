num=int(input('Numar='))
i=2
while(num>i):
    if(num%i==0):
        print('Numarul nu este prim')
        break
    i+=1
if(i==num):
    print('Numarul este prim')
