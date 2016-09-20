# Individual exercise

Take a look at the code for the game war in [war.py](src/war.py) and [war_player.py](src/war_player.py). The code is explained in the [notes](notes.md).

1. Modify the game so that after each round (after each time someone wins the pot) it prints the number of cards each player has like this:

  ```
  Joe has 40 cards and Ann has 12 cards.
  ```
  
  Only do this when the pot is empty, so the values should always add up to 52.
  
  There are tests in test_war.py that fail. Modify war.py to make them pass.

1. Add a property of the war game that allows us to change how many cards will be drawn for each war.
1. Make the game “Best out of 3” instead of just a single game. Look at the tests for some hints about how this should be implemented. You should modify war.py to make the test pass (not the other way around).
