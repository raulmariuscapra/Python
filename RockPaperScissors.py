continues=0
while(continues==0):
    player1 = input("Player1 pick Rock,Paper,Scissors:")
    while((player1 != "Rock") and (player1 != "Paper") and (player1 != "Scissors")):
        if(player1 != "Rock") and (player1 != "Paper") and (player1 != "Scissors"):
            player1 = input("Please only input valid words:")
    player2 = input("Player2 pick Rock,Paper,Scissors:")
    while((player2 != "Rock") and (player2 != "Paper") and (player2 != "Scissors")):
        if(player2 != "Rock") and (player2 != "Paper") and (player2 != "Scissors"):
            player2 = input("Please only input valid words:")
    print("Player1 picked "+ player1)
    print("Player2 Picked "+ player2)
    if(player1 == player2):
        print("Draw")
    elif((player1 == "Rock") and (player2 == "Paper")) or ((player1 == "Paper") and (player2 == "Scissors")) or ((player1 == "Scissors") and (player2 == "Rock")):
        print("Player2 wins")
    elif((player2 == "Rock") and (player1 == "Paper")) or ((player2 == "Paper") and (player1 == "Scissors")) or ((player2 == "Scissors") and (player1 == "Rock")):
        print("Player1 wins")
    cont=input("Do you want to continue?Yes/No:")
    if(cont=="No"):
        continues=1