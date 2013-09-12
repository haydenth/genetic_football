import unittest
from common import Configuration
from common import Player


class ConfigurationTest(unittest.TestCase):

  def test_slots(self):
    """ test we can make a config and add slots """
    slots = ['QB', 'RB1', 'RB2', 'WR1', 'WR2', 'TE', 'FLEX', 'K', 'D']
    config = Configuration(slots, 100)
    self.assertEquals(config.get_slots(), slots)   

  def test_configuration_adding_and_size(self):
    slots = ['QB', 'RB', 'RB', 'WR', 'WR', 'TE', 'FLEX', 'K', 'D']
    config = Configuration(slots, 100000)

    player = Player('Dez Bryant', 'WR', 13.9, 14750)
    player2 = Player('Doug Martin', 'RB', 17.1, 16300)
    config.add_player(player, 'WR1')
    config.add_player(player2, 'RB1')
    self.assertEquals(config.get_value(), 31)
    self.assertEquals(config.get_cost(), 31050)

    self.assertEquals(len(config.get_config()), len(slots))

  def test_adding_a_second_player(self):
    slots = ['QB', 'RB', 'RB', 'WR', 'WR', 'TE', 'FLEX', 'K', 'D']
    config = Configuration(slots, 100000)

    player = Player('Dez Bryant', 'WR', 13.9, 14750)
    player2 = player

    config.add_player(player, 'WR')
    self.assertRaises(BaseException, config.add_player, (player2, 'WR2'))
