import random

class Card:
    r"""Initializes a :class:`Card` Object

    Parameters
    ---------------
    value: :class:`int`
        The value assigned to the card
    face: :class:`str`
        The face value assigned to the card
    suit: :class:`str`
        The suit assigned to the card
    """
    def __init__(self, value:int, face:str, suit:str):
        self.value = value
        self.face = face
        self.suit = suit
    
    def __str__(self):
        return F"{self.suit}{self.face}"

class Deck:
    r"""Initializes a :class:`Deck` object

    Parameters
    ---------------
    number: Optional[:class:`int`]
        The number of decks to be used
    """
    def __init__(self, number:int = 1) -> None:
        if number == 1:
            self.cards = [Card(2, "2", "♠️"),Card(2, "2", "♣️"),Card(2, "2", "♦️"),Card(2, "2", "♥️"),Card(3, "3", "♠️"),Card(3, "3", "♣️"),Card(3, "3", "♦️"),Card(3, "3", "♥️"),Card(4, "4", "♠️"),Card(4, "4", "♣️"),Card(4, "4", "♦️"),Card(4, "4", "♥️"),Card(5, "5", "♠️"),Card(5, "5", "♣️"),Card(5, "5", "♦️"),Card(5, "5", "♥️"),Card(6, "6", "♠️"),Card(6, "6", "♣️"),Card(6, "6", "♦️"),Card(6, "6", "♥️"),Card(7, "7", "♠️"),Card(7, "7", "♣️"),Card(7, "7", "♦️"),Card(7, "7", "♥️"),Card(8, "8", "♠️"),Card(8, "8", "♣️"),Card(8, "8", "♦️"),Card(8, "8", "♥️"),Card(9, "9", "♠️"),Card(9, "9", "♣️"),Card(9, "9", "♦️"),Card(9, "9", "♥️"),Card(10, "10", "♠️"),Card(10, "10", "♣️"),Card(10, "10", "♦️"),Card(10, "10", "♥️"),Card(10, "J", "♠️"),Card(10, "J", "♣️"),Card(10, "J", "♦️"),Card(10, "J", "♥️"),Card(10, "Q", "♠️"),Card(10, "Q", "♣️"),Card(10, "Q", "♦️"),Card(10, "Q", "♥️"),Card(10, "K", "♠️"),Card(10, "K", "♣️"),Card(10, "K", "♦️"),Card(10, "K", "♥️"),Card(11, "A", "♠️"),Card(11, "A", "♣️"),Card(11, "A", "♦️"),Card(11, "A", "♥️")]
        else:
            self.cards = []
            for i in range(number):
                for j in (Card(2, "2", "♠️"),Card(2, "2", "♣️"),Card(2, "2", "♦️"),Card(2, "2", "♥️"),Card(3, "3", "♠️"),Card(3, "3", "♣️"),Card(3, "3", "♦️"),Card(3, "3", "♥️"),Card(4, "4", "♠️"),Card(4, "4", "♣️"),Card(4, "4", "♦️"),Card(4, "4", "♥️"),Card(5, "5", "♠️"),Card(5, "5", "♣️"),Card(5, "5", "♦️"),Card(5, "5", "♥️"),Card(6, "6", "♠️"),Card(6, "6", "♣️"),Card(6, "6", "♦️"),Card(6, "6", "♥️"),Card(7, "7", "♠️"),Card(7, "7", "♣️"),Card(7, "7", "♦️"),Card(7, "7", "♥️"),Card(8, "8", "♠️"),Card(8, "8", "♣️"),Card(8, "8", "♦️"),Card(8, "8", "♥️"),Card(9, "9", "♠️"),Card(9, "9", "♣️"),Card(9, "9", "♦️"),Card(9, "9", "♥️"),Card(10, "10", "♠️"),Card(10, "10", "♣️"),Card(10, "10", "♦️"),Card(10, "10", "♥️"),Card(10, "J", "♠️"),Card(10, "J", "♣️"),Card(10, "J", "♦️"),Card(10, "J", "♥️"),Card(10, "Q", "♠️"),Card(10, "Q", "♣️"),Card(10, "Q", "♦️"),Card(10, "Q", "♥️"),Card(10, "K", "♠️"),Card(10, "K", "♣️"),Card(10, "K", "♦️"),Card(10, "K", "♥️"),Card(11, "A", "♠️"),Card(11, "A", "♣️"),Card(11, "A", "♦️"),Card(11, "A", "♥️")):
                    self.cards.append(j)
    
    def __str__(self) -> str:
        return F"Deck({len(self.cards)} Cards)"
    
    def shuffle(self, number:int = 7) -> None:
        r"""Shuffles the deck

        Parameters
        ---------------
        number: Options[:class:`int`]
            The number of times to shuffle the deck(Defaults to 7)
        """
        for i in range(number):
            random.shuffle(self.cards)
    
    def draw(self) -> Card:
        r"""Draws the top card of the deck, then removes it from the deck"""
        return self.cards.pop(0)
    
    def add_card(self, card:Card) -> None:
        r"""Adds a card to the top of the deck
        
        Parameters
        ---------------
        card: :class:`Card`
            The card you wish to add to the top of the deck
        """
        self.cards.insert(0, card)

class Player:
    r"""Initiates a player"""
    def __init__(self):
        self.hand = []
    
    def deal(self, card:Card) -> None:
        r"""Deal the player a card
        
        Parameters
        ---------------
        card: :class:`Card`
            The card the player is dealt
        """
        self.hand.append(card)

    def blackjack(self) -> bool:
        r"""Determine whether or not the player has BlackJack"""
        if len(self.hand) != 2:
            return False
        ace = False
        face10 = False
        for i in self.hand:
            if i.face == "A":
                ace = True
            if i.face in ("10", "J", "Q", "K"):
                face10 = True
        if ace is True and face10 is True:
            return True
        return False
    
    def total(self) -> int:
        r"""Gets the player's total hand value"""
        value = 0
        for i in self.hand:
            value += i.value
        if value > 21:
            for i in self.hand:
                if i.face == "A":
                    value -= 10
        return value
    
    def bust(self) -> bool:
        r"""Determines whether or not the player busted"""
        if self.total() > 21:
            return True
        return False