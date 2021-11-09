import random

def scriere(x):
    if(x==1):
        print("|X", end='')
    elif(x==2):
        print("|0", end='')
    else:
        print("| ", end='')


#1.Intreaba pe utlizator linia si coloana.
#2.Vezi daca e valid(de la 1 la 3 si daca e deja x sau 0 ceva)
#3.Daca nu este valid pune pe jucator sa dea alta pozite
#4.Daca da atunci pune pe pozitia data x sau 0 depinzand de jucator
#5.Daca unul dintre jucatori a castigat sa opreasca jocul si sa se afiseze cine a castigat
terminat=1
while(terminat==1):
    matrice=[[0,0,0],
    [0,0,0],
    [0,0,0]]
    terminat=False
    castigator=0
    turn=random.randrange(1,3)
    for i in range(0,3):
        print("_______")
        print("| | | |")
    print("_______")
    while(terminat!=True):
        egal=True
        print("Randul jucatorului ",turn)
        valid=False
        while(valid==False):
            lin=int(input("Pe ce linie de la 1 la 3? Lin="))
            col=int(input("Pe ce coloana de la 1 la 3? Col="))
            if(lin>0 and lin<4 and col>0 and col<4 and matrice[lin-1][col-1]==0):
                valid = True
            else:
                print("Introdus gresit")
        matrice[lin-1][col-1]=turn
        for i in range(0,3):
            print("_______")
            scriere(matrice[i][0])
            scriere(matrice[i][1])
            scriere(matrice[i][2])
            print("|")
        print("_______")
        for i in range(0,3):
            if(matrice[i][0]==matrice[i][1] and matrice[i][2]==matrice[i][1] and matrice[i][0]==turn and terminat==False):
                terminat=True
                castigator=turn
        for i in range(0,3):
            if(matrice[0][i]==matrice[1][i] and matrice[2][i]==matrice[1][i] and matrice[0][i]==turn and terminat==False):
                terminat=True
                castigator=turn
        if(matrice[0][0]==matrice[1][1] and matrice[1][1]==matrice[2][2] and matrice[0][0]==turn):
            terminat=True
            castigator=turn
        elif(matrice[0][2]==matrice[1][1] and matrice[1][1]==matrice[2][0] and matrice[2][0]==turn):
            terminat=True
            castigator=turn
        if(terminat==False):
            for i in range(0,3):
                for j in range(0,3):
                    if(matrice[i][j]==0):
                        egal=False
            if(egal==True):
                terminat=True
                castigator=0
        if(turn==1):
            turn=2
        else:
            turn=1
    if(castigator==0):
        print("Remiza")
    else:
        print("Castigatorul este ",castigator)
    terminat=int(input("Pentru a continua apasati tasta 1, iar pentru a opri apasati tasta 0 "))
    while(terminat!=1 and terminat!=0):
        if(terminat!=1 and terminat!=0):
            terminat=int(input("Pentru a continua apasati tasta 1, iar pentru a opri apasati tasta 0 "))