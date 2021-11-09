a=int(input('Primul numar este:'))
b=input('Operatia este(+ ->adunare,- ->scadere,* ->inmultire,/ ->impartire,^ ->putere):')
c=int(input('Al doilea numar este:'))
if(b=='+'):
    print(str(a) + b + str(c) + '=' + str(a+c))
elif(b=='-'):
    print(str(a) + b + str(c) + '=' + str(a-c))
elif(b=='*'):
    print(str(a) + b + str(c) + '=' + str(a*c))
elif(b=='/'):
    print(str(a) + b + str(c) + '=' + str(a/c))
elif(b=='^'):
    print(str(a) + b + str(c) + '=' + str(a**c))
else:
    print('Operatie invalida')
