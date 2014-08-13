from deck import Card, Deck
import nose.tools as n


def test_card_init():
    card = Card("J", "S")
    n.assert_equal(card.number, "J")
    n.assert_equal(card.suit, "S")

def test_card_str():
    card = Card("A", "C")
    n.assert_equal(str(card), "AC")

def test_card_lt():
    card1 = Card("3", "D")
    card2 = Card("8", "D")
    n.assert_less(card1, card2)

def test_card_gt():
    card1 = Card("K", "S")
    card2 = Card("10", "C")
    n.assert_greater(card1, card2)

def test_card_equal():
    card1 = Card("5", "C")
    card2 = Card("5", "H")
    n.assert_equal(card1, card2)

def test_deck_init():
    deck = Deck()
    n.assert_equal(len(deck), 52)
    cards = set()
    for card in deck.cards:
        card_tuple = (card.number, card.suit)
        n.assert_not_in(card_tuple, cards)
        cards.add(card_tuple)

def test_draw_card():
    deck = Deck()
    card = deck.draw_card()
    n.assert_equal(len(deck), 51)
