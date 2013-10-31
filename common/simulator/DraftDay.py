import copy
import random
from common.simulator import Configuration, DefenseList


class DraftDay(object):
  ''' This is the main simulator object - basically it does all the
  magic and simulates the various outcomes '''

  SLOTS = ['QB', 'RB1', 'RB2', 'WR1', 'WR2', 'TE', 'FLEX', 'K', 'D']
  DEFAULT_DEPTH = 50000
  DEFAULT_SALARY_CAP = 100000

  def simulate(self, player_list):
    config = Configuration(self.SLOTS, self.DEFAULT_SALARY_CAP)

    # put random items in the configuration
    for slot in self.SLOTS:
      w = player_list.get_random_player(slot)
      config.add_player(w, slot)

    # now try to simulate to improve the roster
    time_since_last_change = 0
    attempt = 0
    max_config = config

    while time_since_last_change < self.DEFAULT_DEPTH:
      new_config = copy.deepcopy(config)
      time_since_last_change += 1
      attempt += 1

      for number in range(0, random.randint(1, 9)):
        rand_slot = self.SLOTS[random.randint(0, len(self.SLOTS) - 1)]

        w = player_list.get_random_player(rand_slot)
        new_config.add_player(w, rand_slot)

        while new_config.get_cost() > self.DEFAULT_SALARY_CAP:
          w = player_list.get_random_player(rand_slot)
          new_config.add_player(w, rand_slot)

      if new_config.get_value() > config.get_value() - 2:
        config = new_config
        time_since_last_change = 0

      if new_config.get_value() > max_config.get_value():
        max_config = new_config
        config.print_roster('new max!! ' + str(attempt))

    return config
