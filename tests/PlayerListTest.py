import unittest
from common.player import PlayerList
from common.player import Player


class PlayerListTest(unittest.TestCase):
  POSITIONS = ['QB', 'RB', 'WR', 'FLEX', 'D', 'K', 'TE'] 

  def test_failure_on_no_positions(self):
    """ make sure it complains when you dont give a list of positions """
    self.assertRaises(PlayerList)

  def test_basic_player_stuff(self):
    """ test basic attributes on a player """
    name = 'Dez Bryant'
    position = 'WR'
    salary = 14750
    ppg = 13.9
    player = Player(name, position, ppg, salary)

    player_list = PlayerList(PlayerList.POSITIONS)
    player_list.add_player(player)
    player_list.add_player(player)

    self.assertEquals(player_list.get_players()[0], player)
    self.assertEquals(len(player_list.get_players()), 2)

  def test_load_from_file(self):
    """ make sure we can load a draftday file into memory """
    filename = 'tests/draftday_test.csv'
    player_list = PlayerList(PlayerList.POSITIONS)
    player_list.read_from_draftday_csv(filename)
    self.assertEquals(len(player_list.get_players()), 829) 

  def test_random_player(self):
    name = 'Dez Bryant'
    position = 'WR'
    salary = 14750
    ppg = 13.9
    player = Player(name, position, ppg, salary)
    player_list = PlayerList(PlayerList.POSITIONS)
    player_list.add_player(player)
    self.assertEquals(player, player_list.get_random_player(position))

  def test_random_player_with_position_num(self):
    player = Player('Dez Bryant', 'WR', 13.9, 14750)
    player_list = PlayerList(PlayerList.POSITIONS)
    player_list.add_player(player)
    self.assertEquals(player, player_list.get_random_player('WR2'))
