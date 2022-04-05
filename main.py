from classes import Deck, Player

deck = Deck(6)
deck.shuffle()

dealer = Player()
dealer.deal(deck.draw())
dealer.deal(deck.draw())

player = Player()
player.deal(deck.draw())
player.deal(deck.draw())

hand = "Your hand:"
for i in player.hand:
    hand += F"\n{i}"
hand += F"\nTotal Value: {player.total()}\n"
print(hand)

i = True

if dealer.blackjack():
    i = False
    print("The dealer has blackjack! They win")

if player.blackjack() and not dealer.blackjack():
    i = False
    print("You got blackjack! You have won")

while True:
    x = input("Would you like to hit or stand?\n")

    if x.lower() == "hit":
        player.deal(deck.draw())

        hand = "\nYour hand:"
        for i in player.hand:
            hand += F"\n{i}"
        hand += F"\nTotal Value: {player.total()}\n"
        print(hand)

        if player.bust():
            print("You have busted! The dealer wins!")
            break
    elif x.lower() == "stand":
        print("You standed\n")
        for i in range(10):
            if dealer.total() < 17:
                dealer.deal(deck.draw())
                print("Dealer hits\n")
                if dealer.bust():
                    print("Dealer busted! You won\n")
                    break
            else:
                if player.total() > dealer.total():
                    print(F"You win! Your hand: {player.total()} Dealer hand: {dealer.total()}\n")
                    break
                elif player.total() == dealer.total():
                    print(F"Hands equal! Noone wins.  Your hand: {player.total()} Dealer hand: {dealer.total()}\n")
                    break
                else:
                    print(F"Dealer wins! Your hand: {player.total()} Dealer hand: {dealer.total()}\n")
                    break
        break
