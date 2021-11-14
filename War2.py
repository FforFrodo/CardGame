from numpy.random import shuffle
from collections import Counter
 
Suit = ['', '', '', '']
Faces = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
Deck = [f + s for f in Faces for s in Suit]
CARD_TO_RANK = dict((Deck[i], (i + 3) // 4) for i in range(len(Deck)))
 
class WarCardGame:
    """ card game War """
    def __init__(self):
        deck = Deck.copy()
        shuffle(deck)
        self.deck1, self.deck2 = deck[:20], deck[20:]
        self.pending = []
 
    def turn(self):
        """ one turn, may recurse on tie """
        if len(self.deck1) == 0 or len(self.deck2) == 0:
            return self.gameover()
 
        drawpile1 = len(self.deck1)
        drawpile2 = len(self.deck2)
        card1, card2 = self.deck1.pop(0), self.deck2.pop(0)
        rank1, rank2 = CARD_TO_RANK[card1], CARD_TO_RANK[card2]

        print("{}{}{}{:10}".format(
            'Player 1 (', drawpile1, ' cards): ', card1), end='')
        print("{}{}{}{:10}".format(
            'Player 2 (', drawpile2, ' cards): ', card2), end='')
        if rank1 > rank2:
            print('Player 1 wins the round!')
            self.deck1.extend([card1, card2])
            self.deck1.extend(self.pending)
            self.pending = []
        elif rank1 < rank2:
            print('Player 2 wins the round!')
            self.deck2.extend([card2, card1])
            self.deck2.extend(self.pending)
            self.pending = []
        else:  #  rank1 == rank2
            print('Tie!')
            if len(self.deck1) == 0 or len(self.deck2) == 0:
                return self.gameover()
 
            card3, card4 = self.deck1.pop(0), self.deck2.pop(0)
            self.pending.extend([card1, card2, card3, card4])
            print("{:10}{:10}".format("?", "?"), 'Cards are face down.', sep='')
            return self.turn()
 
        return True
 
    def gameover(self):
        """ game over who won message """
        if len(self.deck2) == 0:
            if len(self.deck1) == 0:
                print('\nGame ends as a tie.')
            else:
                print('\nPlayer 1 wins the game.')
        else:
            print('\nPlayer 2 wins the game.')
 
        return False
 
 
if __name__ == '__main__':
    WG = WarCardGame()
    while WG.turn():
        continue

    # Python3 War2.py