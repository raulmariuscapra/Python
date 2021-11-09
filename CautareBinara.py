x=int(input('Numar='))
s=1
c=100
while True:
    numb=int((s+c)/2)
    if(s==99)and(c==100):
        numb=100
    print("Incercare=",numb)
    if(numb>x):
        c=numb
    elif(numb<x):
        s=numb
    else:
        print("Numarul era ",x)
        break