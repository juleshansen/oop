# Object Oriented Programming in Python

In Python, we have a bunch of built-in classes that we use every day. For example, Lists, Strings and Dictionaries are examples. We can create an instance of them and then use methods to operate on them.

We can create a new list or dictionary with what we call a *constructor*:

```python
d = dict()

L = list()

# a more pythonic way of initializing an empty list:
L = []
```

We have methods that allow us to do things with and to the list. A *method* is a function which acts on a class. `append`, `pop` and `extend` are examples of *methods*.

```python
In [1]: L = []

In [2]: L.append('a')

In [3]: L.pop()
Out[3]: 'a'

In [4]: L.extend(['x', 'y', 'z'])

In [5]: L.pop(1)
Out[5]: 'y'
```

The built-in types are very generic and have many uses. However, sometimes we would like to define our own types that fit our specific scenario.


## Card Games as an OOP problem

The example we will be looking at today is creating card games. In this scenario, it's very helpful to have classes to represent a playing card and a deck of cards.

Here is the syntax for creating a card class:

```python
class Card(object):
    def __init__(self, number, suit):
        self.suit = suit
        self.number = number
```

Here the `suit` and `number` are what we call *instance variables*. That means that they are variables that are specific to each *instance* of the class (each card that you create will have its own values for suit and number).

The `__init__` function is the *constructor*. It is called when you run the following code:

```python
card = Card('5', 'C')
```

Look at the deck class for an example where we also create *methods*.

```python
import random

class Deck(object):
    def __init__(self):
        self.cards = []
        for num in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q' 'K', 'A']:
            for suit in 'CDHS':
                self.cards.append(Card(num, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if not self.isempty():
            return self.cards.pop()

    def add_cards(self, cards):
        self.cards.extend(cards)

    def isempty(self):
        return self.cards == []
```

Now we can use our `Deck` class:

```python
In [1]: deck = Deck()

In [2]: deck.draw_card()
Out[2]: AS

In [3]: deck.draw_card()
Out[3]: AH

In [4]: deck.shuffle()

In [5]: deck.draw_card()
Out[5]: QC

In [6]: deck.isempty()
Out[6]: False
```

(Note that with this implementation, the cards go in order until you shuffle the deck.)


## Special methods

In python, there are some special methods that we can implement.

#### Length function

Notice how you can use the `len` function on most built-in types to get the length (length of a list, number of items in a dictionary, length of a string). If you'd like to be able to do the same with your own class, you can implement the `__len__` method.

You can add the following to the `Deck` class:

```python
    def __len__(self):
        return len(self.cards)
```

This enables you to use `len(deck)` and it will give you the number of cards in your deck.

#### Comparisons

You also may want to be able to compare two cards to see which is larger or if they have the same value. You can get this functionality by implementing the '__cmp__' function. 

Here is an implementation of this function for the `Card` class:

```python
   def __cmp__(self, other):
       return cmp(self.value_dict[self.number], self.value_dict[other.number])
```

You can now run the following code:

```python
In [1]: card1 = Card('5', 'C')
In [2]: card2 = Card('7', 'D')
In [3]: card3 = Card('7', 'H')

In [4]: card1 > card2
Out[4]: False

In [5]: card2 == card3
Out[5]: True
```

#### String representation

If you try to print your object, you will get something like this:

```python
In [1]: card = Card('A', 'D')

In [2]: print card
<Card object at 0x10a2ce210>
```

If you would like to be able to print out your object in a human-readable form, you need to create the `__repr__` method which will give the string representation. Here is an example repr method for the `Card` class:

```python
    def __repr__(self):
        return "%s%s" % (self.number, self.suit)
```

Now, this will happen when you try to print the card:

```python
In [1]: card = Card('A', 'D')

In [2]: print card
AD
```

You can of course modify the output however you'd like, putting a space or symbol between the number and suit:

```python
        return "|%s|%s|" % (self.number, self.suit)
```

This gives an output like this: `|A|D|`.


#### Card and Deck implementations

You can find the code for the `Card` and `Deck` classes in [deck.py](code/deck.py).


## How to structure your classes

The hardest part of Object Oriented Programming is figuring out how to structure your classes and what methods you need.

The general rules of thumb are:

* nouns should become classes
* verbs should become methods


## Example: War Card Game

We'll demonstrate how to do this by implementing the children's card game [war](http://en.wikipedia.org/wiki/War_(card_game)).

If you're unfamiliar with the game, read the link or just play the game by running: `python war.py`

It is a complete game of chance, so you will never have to make a decision.

### Classes

We've already created classes for a card and a deck.

The other classes we will need are:

* player
* game

#### The player class

Let's look at the player class. First, what *instance variables* does it need? What does a player need to keep track of?

* `hand`: a list of cards in the player's current deck
* `discard`: a list of cards in the player's discard pile
* `name`: the player's name (not essential)

And what *methods* does the player class need?

* `receive_card`
* `play_card`

The player class is implemented in [war_player.py](code/war_player.py). There are a couple other instance variables and methods there that turned out to be useful that aren't as essential as the ones noted above.

#### The game class

These are the important instance variables:

* `player1` and `player2` (two instances of the `Player` class)
* `pot`: the cards that are currently in play (they will be won by one of the two players at the end of the round)
* `winner`: the player that has won, which will be `None` until the end of the game (this is not the only way to keep track of this information)


These are the important methods:

* `deal`: gives each player their starting decks
* `play_round`: goes through one round of the game (each player plays a card, highest card wins. If they tie, each player plays 3 cards and then they try again.)
* `play_game`: starts the game and calls `play_round` repeatedly until one player gets all the cards and is declared the winner.

When you look at the code in [war.py](code/war.py), you'll notice there are a bunch of other functions. One thing you'll notice is that all of the displaying of the game was separated into separate methods (`display_play`, `display_receive`, `display_war` and `display_winner`). It's nice to separate out the display functions in case later you want to create a fancy UI. Then you don't have to modify any of the game functionality, just the display.

You'll also notice that a few helper methods like `draw_card`, `draw_cards`, `war` and `give_cards` were created to simplify the code for the `play_round` method.
