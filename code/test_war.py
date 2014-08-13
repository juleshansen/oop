import nose.tools as n
from deck import Card
from war import Player, War

def test_player_init():
    player = Player("name")
    n.assert_equal(len(player), 0)
    n.assert_is_none(player.play_card())

def test_player_receive_play():
    player = Player("name")
    card = Card("J", "C")
    player.receive_card(card)
    n.assert_equal(len(player), 1)
    n.assert_equal(player.play_card(), card)
    n.assert_equal(len(player), 0)

def test_war_deal():
    game = War(human=False)
    n.assert_equal(len(game.player1), 26)
    n.assert_equal(len(game.player2), 26)

def test_play_round():
    game = War(human=False)
    game.play_round()
    n.assert_equal(len(game.player1) + len(game.player2), 52)

def test_play_game():
    game = War(human=False)
    game.play_game()
    n.assert_equal(len(game.player1) + len(game.player2) + len(game.pot), 52)
    n.assert_is_not_none(game.winner)
    if game.player1.name == game.winner:
        n.assert_equal(len(game.player2), 0)
    else:
        n.assert_equal(len(game.player1), 0)
