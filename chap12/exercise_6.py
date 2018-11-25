from playingcard import *

class BridgeApp:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        for person in range(4):
            person = Player()
            self.players = person
        self.teamNS = [self.players[0], self.players[2]]
        self.teamEW = [self.players[1], self.players[3]]



class Player:
    def __init__(self):
        self.name
        self.points
        self.currentbid
        self.hand = [] #fill with cards
        
class Bid:
    #Spades, Hearts, Diamonds, Clubs
    #If 3 passes, bidding over / return bidder
    #   first of team to bid wins bid, lest change of suit
    #   
    def __init__(self):
        self.sequence_bids = 
        self.
