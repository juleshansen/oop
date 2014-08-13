# Object Oriented Programming: Blackjack

In this assignment, you'll be implementing the game Blackjack. If you're unfamiliar with the rules of the game, read [this](http://en.wikipedia.org/wiki/Blackjack) or pair yourself with someone who knows them.

We'll start by implementing a simplified version of Blackjack:

1. We'll only have the dealer and the player.
2. You can only hit or stay (no split or double down)

The dealer should play by the rules of hitting at 16 or lower, staying at 17 or higher.


## Starter Code

First take a look at the code we've provided you.

* In `deck.py` there's a `Card` and a `Deck` class.
* `test_deck.py` contains test code for `deck.py`. This can be run with `nosetests test_deck.py`. Take a look at how this is implemented, since you'll want to write tests for your code as well.
* `war.py` and `test_war.py` contain example object oriented code that uses the same `Card` and `Deck` classes you'll be using. It implements the children's game [war](http://en.wikipedia.org/wiki/War_(card_game)). When looking at the code, don't worry about the details of how all the functions are implemented, but take note of what classes were created and what methods they have.


## Before writing code, PLAN!

Before you write any code, you should make a plan of what classes and methods you will implement. It is natural for the plan to be modified a bit as you implement, but you should have a general idea. Just like in the war game, you'll need player classes (how are the dealer and the human player different?) and a game class. What methods will they all need? You might also want some helper functions to do things like calculate the value of the hand.


## Implement and test

As you write your code, you should write test code along side it. Take a look at the example test files for ideas on how to do this.

You should be able to play the game on the command line, by typing in your moves. You can use python's `input` and `raw_input` functions for this.


## Extra Credit

Once you complete it and feel confident that it is correct, you can implement additional features:

** Allow for any number of players
** Implement a computer player
** Implement double down and/or split
