from common.player import Player


class Configuration(object):
  ''' a configuration is a set of slots, where each slot is a position
  that may be occupied by a player. A configuration has a max value that cannot
  be surpassed '''

  def __init__(self, slots, max_allowed_cost):
    self._configuration = {}
    self._slots = slots
    self._max_allowed_cost = max_allowed_cost

    for slot in self._slots:
      self._configuration[slot] = Player('NULL', 'NULL', 0, 0)

  def get_cost(self):
    ''' obtain total cost for players '''
    slot_positions = self._configuration.items()
    return sum([player.get_cost() for (variety, player) in slot_positions])

  def get_slots(self):
    return self._slots

  def get_config(self):
    return self._configuration

  def get_value(self):
    ''' obtain total value for players '''
    slot_positions = self._configuration.items()
    return sum([player.get_value() for (variety, player) in slot_positions])

  def add_player(self, player, slot):
    ''' add a player to a specific slot but dont if they are
    already in a slot. '''
    current_slots = self._configuration.values()
    if player.get_name() in [p.get_name() for p in current_slots]:
      return
    else:
      self._configuration[slot] = player
      return

  def print_roster(self, note=''):
    ''' print out the roster in a nice format '''
    print "========== %s ======= " % note
    for (slot, player) in self._configuration.items():
      print "[%s] %s %s (%f, %s, %s)" % (slot, player.get_name(),
                                         player.get_position(),
                                         player.get_value(),
                                         player.get_cost(),
                                         player.get_opponent())
    print "Total Cost = %d Total Value = %f" % (self.get_cost(),
                                                self.get_value())
