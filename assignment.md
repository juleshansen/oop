# Object Oriented Programming: Blackjack

In this assignment, you'll be implementing the game Blackjack. If you're unfamiliar with the rules of the game, read [this](http://en.wikipedia.org/wiki/Blackjack) or pair yourself with someone who knows them.

We'll start by implementing a simplified version of the game:

1. There should only be the dealer and one player.
1. The player can only hit or stay (no split or double down).

Some notes on the implementation:

1. The dealer should play by the rules of hitting at 16 or lower, staying at 17 or higher.
1. The payout for Blackjack should be 3:2.
1. The player should start with a fixed amount of money, and should be able to play until bankrupt or quitting.


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


## What to Submit

* 'blackjack.py': Running `python blackjack.py` should run your game
* Any other python files you have included (you might want to separate your player code from your blackjack game code)
* `test_blackjack.py`: A set of nose tests of the blackjack game.


## Extra Credit

Once you complete it and feel confident that it is correct, you can implement additional features:

* Allow for any number of players
* Implement a computer player
* Implement double down and/or split
