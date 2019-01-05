import random

#define deck
def deck():

    #create empty deck list
    deck=[]

    #take suits and rank and append in empty deck list
    for suit in ['H','S','D','C']:
        for rank in ['A','2','3','4','5','6','7','8','9','T','J','Q','K']:
            deck.append(suit+rank)

    #shuffle the deck
    random.shuffle(deck)
    return deck


# Takes in player's card and returns his total points.
def pointcount(mycards):
    
    totalcount=0
    acecount=0

    for i in mycards:

        #value for 10,j,q,k is 10 .. add it to total count
        if (i[1] == 'T' or i[1] == 'J' or i[1] == 'Q' or i[1] == 'K'):
            totalcount+=10
        
        #value is number .. add it to total count
        elif (i[1]!='A'):
            totalcount+=int(i[1])
        
        #value is an ace .. then add it to ACECOUNT
        else:
            acecount+=1
        
    #calculate the value of ace if it's 1 or 11.
    #if there's only 1 ace and total is 10+ then ace value is 11
    if(acecount==1 and totalcount>=10):
        totalcount+=11
    
    #if more than 1 ace then ace value is 1
    elif(acecount != 0):
        totalcount+=1

    return totalcount
         

#create player and dealer's hands. Give them 2 cards each.
#return a list with both hands.
def createplayinghands(mydeck):
    dealerhands=[]
    playerhands=[]

    dealerhands.append(mydeck.pop())
    dealerhands.append(mydeck.pop())
    playerhands.append(mydeck.pop())
    playerhands.append(mydeck.pop())

    while (pointcount(dealerhands) <=16):
        dealerhands.append(mydeck.pop())

    return [dealerhands,playerhands]


#game
game= " "
mydeck=deck()
hands=createplayinghands(mydeck)
dealer=hands[0]
player=hands[1]

while (game != "exit"):
    dealercount=pointcount(dealer)
    playercount=pointcount(player)

    print("dealer has: {}".format(dealer[0]))
    print ("player has: {}".format(player))

    if (playercount==21):
        print("player wins! with {} points".format(playercount))
        break

    elif (playercount >21):
        print("player busts!!! with {} points. Dealer wins!".format(playercount))
        break

    elif (dealercount > 21):
        print("dealer busts!!! with {} points. Player wins!".format(dealercount))
        break
    
    game = input("What would you like to do? H: HIT \nS:Stand\n")

    if (game=='H'):
        player.append(mydeck.pop())

    elif(playercount>dealercount):
        print("player wins! with {} points".format(playercount))
        print("dealer has {} or {} points".format(dealer,dealercount))
        break

    else:
        print("Dealer wins!")
        print("dealer has {} or {} points".format(dealer,dealercount))
        break

    
    


