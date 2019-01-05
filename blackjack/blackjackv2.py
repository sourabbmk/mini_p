import random

#dealer cards
dealercards=[]

#player cards
playercards=[]

#deal the cards
#display the cards
#dealer cards

while(len(dealercards)!=2):
    dealercards.append(random.randint(1,11))
    if (len(dealercards)==2):
        print("dealer has: X & {}".format(dealercards[1]))

#player cards

while(len(playercards)!=2):
    playercards.append(random.randint(1,11))
    if (len(playercards)==2):
        print("player has: {}".format(playercards))


#sum of player cards

while ((sum(playercards)<21) and (sum(dealercards)<21)):
    action=str(input("Do you want to stay or hit?"))
    if action.lower() == 'h' or action.lower() == 'hit':
        playercards.append(random.randint(1,11))
        dealercards.append(random.randint(1,11))
        
        print("you have a total of "+str(sum(playercards))+" from these cards {}".format(playercards))
    else:
        print("the dealer has a total of "+str(sum(dealercards))+" with {}".format(dealercards))
        print("the player has a total of "+str(sum(playercards))+" with {}".format(playercards))

        if sum(dealercards)>sum(playercards):
            print("dealer wins!")
            break
        else:
            print("player wins!")
            break

if sum(playercards)>21:
    print("player busted. Dealer wins!!")
    print("player's value= {} and the cards are ={}".format(sum(playercards),playercards))
    print("dealer's value= {} and the cards are ={}".format(sum(dealercards),dealercards))
elif sum(playercards)==21:
    print("player has blackjack!!! player wins!! 21")
    print("dealer's value= {} and the cards are ={}".format(sum(dealercards),dealercards))
    print("player's value= {} and the cards are ={}".format(sum(playercards),playercards))

#sum of dealer cards
if sum(dealercards) == 21:
    print("dealer has 21 and wins!")
    print("player's value= {} and the cards are ={}".format(sum(playercards),playercards))
    print("dealer's value= {} and the cards are ={}".format(sum(dealercards),dealercards))

elif sum(dealercards) >21:
    print("dealer has busted. Player wins!!")
    print("player's value= {} and the cards are ={}".format(sum(playercards),playercards))
    print("dealer's value= {} and the cards are ={}".format(sum(dealercards),dealercards))
        