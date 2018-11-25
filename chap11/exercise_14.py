from playingcard import PlayingCard
from random import random
from graphics import GraphWin, Point
from time import sleep

def isFlush(hand):
    for i in hand:
        x = hand.count(i)
        if x == 5:
            return True
        else:
            return False

def isStraight(hand):
    for i in range(len(hand) - 1):
        if hand[i] + 1 != hand[i+1]:
            return False
    return True
   
def isFourKind(hand):
    for i in hand:
        x = hand.count(i)
        if x == 4:
            return True
        elif x >= 2:
            return False
            
def isFullHouse(hand):
    hand = isPair(hand)
    for i in hand:
        if hand.count(i) == 3:
            return True
        else:
            return False
            
def isThreeKind(hand):
    for i in hand:
        if hand.count(i) == 3:
            return True

def isTwoPair(hand):    
    for i in hand:
        if hand.count(i) == 2:
            return True
        elif hand.count(i) > 2:
            return hand

def isPair(hand):
    for i in hand:
        if hand.count(i) == 2:
            for x in range(2):
                hand.remove(i)
            return hand
        elif hand.count(i) > 2:
            return hand

def XHigh(hand):
    rank = ['', "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    hand.sort()
    return rank[hand[4] - 1]

def shuffle(myList):
    newList = []
    for i in range (len(myList)):
        x = int(random() * len(myList)) - 1
        newList.append(myList[x])
        myList.remove(myList[x])
    return newList

def main():
    win = GraphWin("Playing Card", 700, 1100)
    win.setCoords(-10, -10, 10, 10)
    
    #create 52 card (13 per suit) parameters    
    rank = ['C','D','H','S']
    cardSpecs = []
    for i in range(52):
        x = i % 13 + 1
        y = rank[i % 4]
        cardSpecs.append((x,y))
    cards = []
    for (x, y) in cardSpecs:
        cards.append(PlayingCard(x, y))
   
    #shuffle deck
    cards = shuffle(cards)
    
    #Create a poker hand of 5
    handRank = []
    handSuit = []
    for card in cards[0:5]: 
        card.draw(win, Point(0,0))
        sleep(1)
        handRank.append(card.getRank())
        handSuit.append(card.getSuit())
    
    #Align Cards in rank order
    handRank.sort()
    if handRank[0] == 1:
        handRank[0] = 14
        handRank.sort()
    print(handSuit)
    print(handRank)
    
    #Evaluate hand
    if isFlush(handSuit):
        if isStraight(handRank): 
            if XHigh(handRank) == 'Ace':
                print("Royal Flush")
            else:
                print("Straight Flush")
        else:
            print("Flush")
    elif isStraight(handRank):
        print("Straight")
    elif isThreeKind(handRank):
        if isFullHouse(handRank):
            print("Full House")
        else:
            print("Three of a Kind")
    elif isPair(handRank):
        if isTwoPair(handRank):
            if isFourKind(handRank):
                print("Four of Kind")
            else:
                print("Two Pair")
        else:
            print("Pair")
    else:
        xhigh = XHigh(handRank)
        print(xhigh, "high")

main()