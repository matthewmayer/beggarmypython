def penalty_value_of(card):
    values = {"J":1,"Q":2,"K":3,"A":4}
    return values[card]

def play(hands,firstCardOnLeft=True,verbose=False):
    a,b = hands #hands are called a and b
    a = list(a)
    b = list(b)
    #print "Starting hands: %s/%s" % (a,b)
    if not firstCardOnLeft:
        a.reverse()
        b.reverse()
    stack = list() #cards in the middle
    turns = 0
    tricks = 0
    player = 1 #alternates between 1 and -1
    while len(a)>0 and len(b)>0: #game terminates when a or b's hands are empty
        battle_in_progress = False
        cards_to_play = 1
        while cards_to_play>0: #current player may play up to cards_to_play cards
            turns=turns+1
            
            try:
                if player==1:
                    #grab next card from first character of string a
                    next_card = a.pop(0)
                else:
                    #grab next card from first character of string b
                    next_card = b.pop(0)
            except IndexError:
                break #ran out of cards to play, game over...
            
            stack.append(next_card) #add to the stack
            
            if next_card=='-':
                #not a court card
                if battle_in_progress:
                    cards_to_play=cards_to_play-1 #this player needs keep trying to find a court card
                else:
                    player = player*-1 #no court cards found yet, back to other player
            else:
                #court card found, back to the other player
                battle_in_progress = True 
                cards_to_play = penalty_value_of(next_card)
                player = player*-1
                
        #end of trick, make the losing player pick up the cards in the stack
        tricks = tricks+1
        if player==1:
            b = b+stack 
            stack = list()
        else:
            a = a+stack 
            stack = list()
        
        
        player = player*-1
        
        #print current status
        #if verbose:
            #print "%s/%s/%s" % (a,b,stack)
        
    #print "There were %d turns" % turns
    #print "There were %d tricks\n" % tricks
    return (turns,tricks)
    