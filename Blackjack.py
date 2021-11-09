import random

def cartiplayer():
    carti=["2","3","4","5","6","7","8","9","10","A","J","Q","K"]
    ass=0
    player=[0,0,0,0,0,0,0,0,0,0,0,0,0]
    scriereplayer=[0,0,0,0,0,0,0,0,0,0,0,0,0]
    scriereplayer[0]=random.randint(2,14)
    if(scriereplayer[0]>11):
        player[0]=10
    else:
        player[0]=scriereplayer[0]
    scriereplayer[1]=random.randint(2,14)
    if(scriereplayer[1]>11):
        player[1]=10
    else:
        player[1]=scriereplayer[1]
    print("Mana Ta:" + carti[scriereplayer[0]-2] + "  " + carti[scriereplayer[1]-2])
    nrcarti=2
    sumplayer=player[0]+player[1]
    if(player[0]==11)and(player[1]==11):
        sumplayer=sumplayer-10
    if(player[0]==11 or player[1]==11):
        ass=1
    elif(player[0]==11 and player[1]==11):
        ass=2
    print("Valoarea este:")
    print(sumplayer)
    adaugare=1
    if(sumplayer==21):
        print("Bravo ai facut BlackJack")
        adaugare=0
    else:
        adaugare=int(input("___Daca doriti sa va opriti apasati tasta 0: "))
    while(adaugare==1):
        scriereplayer[nrcarti]=random.randint(2,14)
        if(scriereplayer[nrcarti]>11):
            player[nrcarti]=10
        else:
            player[nrcarti]=scriereplayer[nrcarti]
        sumplayer=sumplayer+player[nrcarti]
        if(player[nrcarti]==11):
            ass=ass+1
        nrcarti=nrcarti+1
        if(sumplayer>21)and(ass>0):
            sumplayer=sumplayer-10
            ass=ass-1
        print("Mana ta este:")
        for i in range(0,nrcarti):
            print(carti[scriereplayer[i]-2])
        print("Valoarea este")
        print(sumplayer)
        if(sumplayer==21):
            print("Bravo ai facut BlackJack")
            adaugare=0
        elif(sumplayer>21):
            print("Valoarea este prea mare")
            adaugare=0
        else:
            adaugare=int(input("____Daca doriti sa va opriti apasati tasta 0: "))
    return sumplayer

carti=["2","3","4","5","6","7","8","9","10","A","J","Q","K"]
continues=1
dealer=[0,0,0,0,0,0,0,0,0,0,0,0,0]
scrieredealer=[0,0,0,0,0,0,0,0,0,0,0,0,0]
sumpplayer=[0,0,0,0,0,0,0,0,0,0,0,0]
summax=0
sumadealer=0
imax=[0,0,0,0,0,0,0,0,0,0]
jucatoricastig=0
nrcartidealer=2
abonare=[0,0,0,0,0]
while(continues==1):
    i=0
    while(dealer[i]!=0):
        dealer[i]=0
        i+=1
    summax=0
    jucatori=int(input("Numar jucatori maxim 5: "))
    if(jucatori>5):
        jucatori=int(input("Numar jucatori maxim 5: "))
    scrieredealer[0]=random.randint(2,14)
    if(scrieredealer[0]>11):
        dealer[0]=10
    else:
        dealer[0]=scrieredealer[0]
    scrieredealer[1]=random.randint(2,14)
    if(scrieredealer[1]>11):
        dealer[1]=10
    else:
        dealer[1]=scrieredealer[1]
    print("Mana dealerului: " +carti[scrieredealer[0]-2] )
    if(dealer[0]==11):
        print("Doriti sa va abonati la dealer?")
        for i in range(0,jucatori):
            print("Jucatorul "+str(i+1))
            abonare[i]=int(input("Apasa tasta 1 pentru a te abona "))
        print("Mana dealerului: " +carti[scrieredealer[0]-2]+"   "+carti[scrieredealer[1]-2])
        if(dealer[0]+dealer[1]==21):
            for i in range(0,jucatori):
                if(abonare[i]==1):
                    print("Jucatorul cu numarul "+ str(i+1) +" a castigat")
        else:
            print("Jucatorul cu numarul "+ str(i+1) +" a pierdut")
    else:
        for i in range(0,jucatori):
            print("Jucatorul ")
            print(i+1)
            sumpplayer[i]=cartiplayer()
            if(sumpplayer[i]<=21)and(sumpplayer[i]==summax):
                imax[jucatoricastig+1]=i
                jucatoricastig=jucatoricastig+1
            if(sumpplayer[i]<=21)and(sumpplayer[i]>summax):
                summax=sumpplayer[i]
                imax[0]=i
                jucatoricastig=0
        ass=0
        print("Mana dealerului: " +carti[scrieredealer[0]-2]+"   "+carti[scrieredealer[1]-2])
        if(dealer[0]==11 or dealer[1]==11):
            ass=ass+1
        sumadealer=dealer[0]+dealer[1]
        print("Valoarea dealerului este")
        print(sumadealer)
        while(sumadealer<17) and (summax!=0) and (sumadealer!=21):
            scrieredealer[nrcartidealer]=random.randint(2,14)
            if(scrieredealer[nrcartidealer]>11):
                dealer[nrcartidealer]=10
            else:
                dealer[nrcartidealer]=scrieredealer[nrcartidealer]
            sumadealer=sumadealer+dealer[nrcartidealer]
            if(dealer[nrcartidealer]==11):
                ass=ass+1
            if(sumadealer>21 and ass>0):
                sumadealer=sumadealer-10
                ass=ass-1
            nrcartidealer=nrcartidealer+1
            print("Mana dealerului este:")
            for i in range(0,nrcartidealer):
                print(carti[scrieredealer[i]-2])
            print("Valoarea dealerului este")
            print(sumadealer)
        if(summax==sumadealer):
            print("Push")
        if(summax==0)and(sumadealer>21):
            print("Push")
        if(sumadealer<=21)and(summax==0):
            print("Dealerul a castigat ")
        if(summax<sumadealer)and(sumadealer<=21) and(summax!=0):
            print("Dealerul a castigat ")
        if(jucatoricastig>=0)and (summax>sumadealer)and(summax>0):
            for i in range(0,jucatoricastig+1):
                print("Jucatorul "+str(imax[i]+1)+" a castigat cu valoarea de "+str(summax))
        if(jucatoricastig>=0)and (sumadealer>21)and(summax>0):
            for i in range(0,jucatoricastig+1):
                print("Jucatorul "+str(imax[i]+1)+" a castigat cu valoarea de "+str(summax))
    continues=int(input("___1->Pentru a continua,0->pentru a te opri "))
