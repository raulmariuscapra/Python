limit = int(input('Limita='))
prev = False
prevpatr = 0
for i in range(1,limit):
    patr=i*i
    if(patr>limit):break
    if(patr>prevpatr):
        prevpatr=patr
        print(patr)
        prev = True
    elif (prev is True) and (patr==prevpatr):
        prev=False
