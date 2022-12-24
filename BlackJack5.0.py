# Blackjack4.0, modified from BlackJack3.0

# What needs to be imported into the program:

import random

# This is the list to keep track of used cards
deck_list = [0,0,0,0,0,0,0,0,0,0,0,0,0]


# Functions to be used in the main

# These functions are good
def intro():
    print("Welcome to BlackJack4.0!")
    playing = input("Are you ready to begin playing? ")
    playing = playing.lower()
    return playing

def setcredit():
    credit = int(input("Please enter your total credit: "))
    return credit

def setwager(x):
    wager = int(input("Please enter your wager: "))
    while wager > credit:
        wager = int(input("That is more than your credit, please enter your wager: "))
    return wager

def returnvalue1(x):
    if x>10:
        return 10
    elif x == 1:
        return 11
    else:
        return x

def checkdeck(x, card):
        x[card-1] += 1
        if x[card-1] == 5:
            return False
        else:
            return True

def setcard(x):
    card = random.randint(1,13)
    check = checkdeck(x, card)
    while check != True:
        card = random.randint(1,13)
        check = checkdeck(x, card)
    return returnvalue1(card)

def doubledown(x):
    if int(x) >= 8:
        decision = input("Would you like to double down? ")
        decision = decision.lower()
        if decision.lower() == "yes":
            return 2
        else:
            return 1
    else:
        return 1

def isitbust(x):
    if x>21:
        return True
    else:
        return False

def lost(x,y):
    print("You lost!")
    x -= y
    print("Your new credit is:", x)
    return x

def won(x,y):
    print("You won!")
    x += y
    print("Your new credit is:", x)
    return x

def checkforAce(ace, x):
    if x == 11 or ace == True:
        return True
    else:
        return False

# Idk about these functions, don't use them in the program
def player_ace(ace, total, card):
    if ace== True:
        if card == 11:
            if total + card >21:
                return total +1
            else:
                return total +11
        else:
            if total + card > 21:
                return total + card - 10
    else:
        return total + card

def dealer_ace(card, total):
    if checkforAce(card)== True:
        if total + 11 >21:
            return total +1
        else:
            return total +11
    else:
        return total + card

# Main program

playing = intro()

credit_original = setcredit()
credit = credit_original

while playing == "yes":

    ace1 = False

    wager = setwager(credit)

    dealer_card1 = setcard(deck_list)
    
    print("The dealers first card is:", dealer_card1)

    card1 = setcard(deck_list)

    ace1 = checkforAce(ace1, card1)

    print("Your first card is:", card1)

    if credit >= wager *2:
        wager = wager * doubledown(card1)

    card2 = setcard(deck_list)

    ace1 = checkforAce(ace1, card2)

    print("Your second card is:", card2)

    player_total = card1 + card2

    print("Your player total is:", player_total)

    if player_total == 21:
        credit = won(credit, wager)
    else:

        if player_total < 21:
            decision = input("Hit or stand? ")
            decision = decision.lower()
        while decision == "hit" and player_total<21:  
            card = setcard(deck_list)
            print("Your next card is:", card)
            player_total += card
            ace1 = checkforAce(ace1, card)
            if ace1 == True:
                if player_total>21:
                    player_total -= 10
                    ace1 = False
            print("Your player total is:", player_total)
            if player_total<21:
                decision = input("Hit or stand? ")
                decision = decision.lower()

        if isitbust(player_total) == True:
            credit = lost(credit, wager)
        else:
            ace1 = False
            ace1 = checkforAce(ace1, dealer_card1)
            dealer_total = dealer_card1
            while dealer_total < 17:
                card = setcard(deck_list)
                ace1 = checkforAce(ace1, card)
                dealer_total += card
                if ace1 == True:
                    if dealer_total>21:
                        dealer_total -= 10
                        ace1 = False
                print("The dealer's next card is:", card)
                
        
            print("Final dealer total:", dealer_total)
            if dealer_total >21 or (dealer_total <=21 and player_total>dealer_total):
                credit = won(credit, wager)
            elif dealer_total == player_total:
                print("Push")
                print("Your new credit is:", credit)
            else:
                credit = lost(credit, wager)
    if credit == 0:
        print("You have run out of credit!")
        playing == "no"
    else:
        playing = input("Would you like to continue to play: ")

print("You finished with", credit, "credit!")
if credit_original > credit:
    print("This means you owe: $", credit_original-credit)
elif credit_original == credit:
    print("You broke even!")
else:
    print("This means you profited: $", credit - credit_original)


# This now just does not have the split option
