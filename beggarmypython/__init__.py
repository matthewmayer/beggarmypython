# -*- coding: utf-8 -*-
def penalty_value_of(card):
    values = {"J": 1, "Q": 2, "K": 3, "A": 4}
    return values[card]


def substitute(hand):
    # replace - with greek and cyrillic letters so we can see how non-court cards permute
    gl = 'αβγδεζηθιλμνξοπρστυφχψωбвгджзилцчшщъыьэюя'
    nextindex = 0
    hand = list(hand)
    for i in range(len(hand)):
        if hand[i] == '-':
            hand[i] = gl[nextindex]
            nextindex += 1
    return ''.join(hand)


def play(hands, firstCardOnLeft=True, verbose=False, substituteValuesForNonCourtCards=False):
    if substituteValuesForNonCourtCards:
        a, b = hands
        hands = (substitute(a), substitute(b))

    (turns, tricks, finite, loopData) = calculate(
        hands, firstCardOnLeft, verbose)
    if finite:
        print("There were %d turns" % turns)
        print("There were %d tricks\n" % tricks)
    else:
        print("Game appears to be infinite, loop detected after %d turns and %d tricks" % (
            turns, tricks))
        (startTurn, startTrick) = loopData
        print("- the loop is %d turns and %d tricks long" %
              (turns-startTurn, tricks-startTrick))


def calculate(hands, firstCardOnLeft=True, verbose=False):
    a, b = hands  # hands are called a and b
    print("Starting hands: %s/%s" % (a, b))
    if not firstCardOnLeft:
        a.reverse()
        b.reverse()
    stack = ""  # cards in the middle
    turns = 0
    tricks = 0
    player = 1  # alternates between 1 and -1
    finite = True
    visited = set()  # keep the visited statuses
    visitedmap = {}
    while a != "" and b != "" and finite:  # game terminates when a or b's hands are empty
        battle_in_progress = False
        cards_to_play = 1
        while cards_to_play > 0:  # current player may play up to cards_to_play cards

            try:
                if player == 1:
                    # grab next card from first character of string a
                    next_card = a[0]
                    a = a[1:]
                else:
                    # grab next card from first character of string b
                    next_card = b[0]
                    b = b[1:]
            except IndexError:
                break  # ran out of cards to play, game over...

            turns = turns+1

            stack = stack+next_card  # add to the stack

            if next_card not in ['A', 'K', 'Q', 'J']:
                # not a court card
                if battle_in_progress:
                    # this player needs keep trying to find a court card
                    cards_to_play = cards_to_play - 1
                else:
                    player = player * -1  # no court cards found yet, back to other player
            else:
                # court card found, back to the other player
                battle_in_progress = True
                cards_to_play = penalty_value_of(next_card)
                player = player * -1

        # end of trick, make the losing player pick up the cards in the stack
        tricks = tricks+1
        if player == 1:
            b = b+stack
            stack = ''
        else:
            a = a+stack
            stack = ''

        player = player*-1

        # print current status
        status = "%s/%s/%s" % (a, b, stack)
        if verbose:
            print(status)

        # check for finiteness
        if status in visited:
            finite = False
        else:
            visited.add(status)
            visitedmap[status] = (turns, tricks)
    return (turns, tricks, finite, visitedmap[status])
