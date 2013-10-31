import csv


class DefenseList(object):
  ''' This class holds the data structures for a defensive override
  for changing player performance depending on opposing defenses '''

  _CUSTOM_FIELDS = ['team', 'expected_pa', 'player_adjustment']

  def __init__(self):
    self.defenses = {}

  def add_defense(self, team, expected_pa, player_adjustment):
    self.defenses[team] = {'expected_pa': expected_pa,
                           'player_adjustment': player_adjustment}

  def read_from_custom(self, filename):
    handler = open(filename, 'r')
    csv_reader = csv.DictReader(handler, self._CUSTOM_FIELDS, delimiter=',')
    for line in csv_reader:
      self.add_defense(line['team'], line['expected_pa'],
                       line['player_adjustment'])
    handler.close()

  def get_adjustment(self, team):
    return self.defenses[team]['player_adjustment']
