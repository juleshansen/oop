# Object Oriented Programming in Python

In programming, there are typically two dominant paradigms to structure code: Functional and Object Oriented.  Functional programming eschews mutable state, i.e. variables, and passes information/logic through the input and output of functions. OO programming on the other hand embraces state (i.e. remembering) in the form of variables and objects.  For example, if I wanted to write a program that calculates some mathematical results, I might pass intermediate values from one function to the next through an internal variable.  

Often a language chooses to focus on one, [Java](http://docs.oracle.com/javase/tutorial/java/concepts/) is almost purely OO (although that is changing with recent versions) in that you cannot even write a function outside of a class.  Others are purely functional in that you are prevented from creating variables.  Many language leverage the strengths of both of these paradigms, Python included.

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

## Primer on Classes

Think of a class as a blueprint.  It is a scaffold for an house we would like to build.  And since we might want to create many houses that all are very similar (though might have a few properties that differ such as color, siding, porch, etc.) we want to remember how to easily build more houses.  The class is this blueprint and an object instantiation is an individual physical house.

## Data and Computation (Nouns and Verbs)

### Object Oriented

In OO programming, Objects are the 'first class citizen' which encapsulate both data (state) and computation.  These are separated as variables and methods.  Programs are simply a collection of objects that pass state around through 'messages' (i.e. method calls).  Methods are functions that operate on state (data) to mutate an object.  Let us unpack that a bit.

![messages](http://2.bp.blogspot.com/-N2sHRubepUE/T3rFv_IjeYI/AAAAAAAAABc/qyetT9SvixU/s1600/OOP000%5B1%5D.jpg)

In plain English... when you call a method on an object, you send a message to it through its arguments (or lack thereof) to update its internal state (variables).  `mean()` in the code above tells the `Variance` object to update its internal state: `self.total_length` and `self.mean`.

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
            for suit in 'cdhs':
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
In [1]: card1 = Card('5', 'c')
In [2]: card2 = Card('7', 'd')
In [3]: card3 = Card('7', 'h')

In [4]: card1 > card2
Out[4]: False

In [5]: card2 == card3
Out[5]: True
```

#### String representation

If you try to print your object, you will get something like this:

```python
In [1]: card = Card('A', 'd')

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
In [1]: card = Card('A', 'd')

In [2]: print card
Ad
```

You can of course modify the output however you'd like, putting a space or symbol between the number and suit:

```python
        return "|%s|%s|" % (self.number, self.suit)
```

This gives an output like this: `|A|d|`.


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


## Testing!

We will be using `nose` to test our code. The syntax is very simple. Basically, you need to write a function for each test you want to run. The challenge is to determine what the necessary tests are.

When writing tests, you want to think about all the edge cases and make sure your code won't break. For example, for the `Card` and `Deck` classes, you want to test the following things:

* Initializing a card sets the number and suit correctly
* You get the correct string representation of a card
* Comparisons work correctly (<, >, ==)
* The deck is initialized correctly (has 52 unique cards)
* Drawing a card works (you get a card and now the deck has one less card)

You can use tests to make sure that you are implementing your code correctly and also to make sure that when you implement additional features you don't break anything.

You can find test examples in [test_deck.py](code/test_deck.py) and [test_war.py](code/test_war.py).

# Appendix

### Functional vs. OOP

In functional programming, state never changes (programs are stateless).  Functions are 'first class citizens' and can actually be passed around like variables, used as arguments to a function, etc. (think `map()`, `reduce()`, `filter()`). Functions (and a program at large) is a series of operation to perform on an immutable data source. And functions can be passed around like data!

### (Functional) Python
```python
def mean(data):
    return reduce(float.__add__, data)/len(data)

def sum_squared_error(data, mean):
    return reduce(float.__add__, [ math.pow(num - mean, 2) for num in data])/len(data)

def variance(data):
    return sum_squared_error(data, mean(data))

variance([1.,2.,3.,4.]) #=> 1.25
```

### (Object Oriented) Python
```python
class Variance(object):
    def __init__(self, input_list):
        self.data = input_list
        self.total_length = 0
        self.difference_sum = 0

    def mean(self):
        total = 0.0
        for num in self.data:
            total += num
            self.total_length += 1
        self.mean = total/self.total_length

    def sum_squared_error(self):
        for num in self.data:
            self.difference_sum += math.pow(num - self.mean, 2)
        self.variance = self.difference_sum / self.total_length

    def compute_variance(self):
        return self.variance

variance_object = Variance([1.,2.,3.,4.])
variance_object.mean()
variance_object.sum_squared_error()
variance_object.compute_variance() #=> 1.25
```

__NOTE: There is no wrong paradigm, they both have their strengths and weaknesses__

## Three principles of OO programming (or something)

I think that any rigid formalism around the 'tenets' of proper OO design is a little contrived... but people often refer to the 3 principles (read: benefits) of design:

1. Encapsulation
2. Polymorphism
3. Inheritance

_source: [https://python.g-node.org/python-summerschool-2013/_media/wiki/oop/oo_design_2013.pdf](https://python.g-node.org/python-summerschool-2013/_media/wiki/oop/oo_design_2013.pdf)_

### Encapsulation

Encapsulation allows you to create proper abstractions and abstractions are _THE_ most powerful concept of computer science.  Encapsulation is the practice of only exposing what is necessary to the outside world (i.e. code outside of your class).  Think of the methods and instance variables as the interface into the code contained within the object.  This lets the programmer dictate how their code is used and actually can force people to think differently.  One of my favorite examples of good OO design principles is within the `scikit-learn` library.  Do not worry if you do not understand any of the code here or the algorithms implemented... that is the joy of OO design and proper encapsulation.

All you have to understand is the following concepts:

> A machine learning model is an interface.  It takes data and labels.  From these data and labels it learns what patterns are associated with what labels.  This process is called fitting (or training) a model.  If you then give it data without labels, it can predict what those labels should be.  This is all we need to know and the library has properly abstracted all the messy details from us.


```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

iris = load_iris()

# get data and labels
X, y = iris.data, iris.target

# create a classifier object.  
clf = KNeighborsClassifier(n_neighbors=1)

# Initialization state == number of neighbors.
# this takes some domain knowledge of the internals of
# the object.  Most libraries use sane defaults however
# 
# clf = KNeighborsClassifier()

# Train our classifier model (change internal state)
clf.fit(X, y)

# predict on new values
y_pred = clf.predict(new_data)
```

Notice how `.fit()` did not return any value?  If this were a functional interface, data would go in and a trained model would come out.  `scikit-learn` adheres to many principles of good OO design and because of this, `.fit()` simply mutates the internal state of the classifier.  It is in this internal state (variables) that the trained model (and its parameters) resides.

### Inheritance (extensibility)

![inheritance](http://techsharer.com/wp-content/uploads/2013/11/TIJ308.png)

Inheritance is the ability of one class to override behavior of its 'parent' class to allow for customized behavior.  With inheritance, a 'child' class has all of the features and functionality (methods) of its 'parent' unless explicitly overriden.  Stepping away from our `scikit-learn` example for a second here, I will demonstrate inheritance with a much simpler example.

```python
class Animal(object):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print "My name is " + self.name

    def eat(self, food):
        print "I love " + food

frank = Animal("Frank")
frank.speak() #=> "My name is Frank"
frank.eat("bananas") #=> "I love bananas"

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def eat(self):
        print "I like biscuits!"

fido = Dog("Fido")
fido.speak() #=> "My name is Fido"
fido.eat() #=> "I like biscuits!"
```

### Polymorphism

Related to (empowered by) inheritance, polymorphism enables us to use a shared interface for similar objects, while still allowing each object to have its own specialized behavior. It does this through inheritance of a common parent and subclassing.

> Polymorphism refers to a programming language's ability to process objects differently depending on their data type or class. More specifically, it is the ability to redefine methods for derived classes.

For `scikit-learn` this simply means that the internals of the model you are training can be drastically different (i.e. kNN vs. Decision Tree) but the methods you call for each are identical.

```python
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

iris = load_iris()

# get data and labels
X, y = iris.data, iris.target

# create a kNN classifier object.  
clf = KNeighborsClassifier(n_neighbors=1)

# Train our classifier model
clf.fit(X, y)

# predict on new values
y_pred = clf.predict(new_data)

# Decide we want to experiment with a DecisionTree
clf = tree.DecisionTreeClassifier()

# Train our classifier model
clf.fit(X, y)

# predict on new values
y_pred = clf.predict(new_data)
```
Notice that since a DecisionTree model and kNN model both have a `fit()` method defined that takes the same inputs (or many of the same), we can optimistically call `fit()` on whatever type of model the `clf` variable references.  This allows us to do some pretty powerful things with our models (i.e. GridSearch parameter optimization) which we will see later in the course.
