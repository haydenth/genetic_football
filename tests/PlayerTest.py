import unittest
from common import Player


class PlayerTest(unittest.TestCase):

  def test_attributes(self):
    """ test basic attributes on a player """
    name = 'Dez Bryant'
    position = 'WR'
    salary = 14750
    ppg = 13.9

    player = Player(name, position, ppg, salary)
    self.assertEquals(player.get_name(), name)
    self.assertEquals(player.get_position(), position)
    self.assertEquals(player.get_value(), ppg)
    self.assertEquals(player.get_cost(), salary)
