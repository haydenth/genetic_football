import csv
import re
import random
from common import Player
from common import Teams
from common import DefenseList


class PlayerList(object):

  DRAFTDAY_FIELDS = ['position', 'player_name', 'team', 'opp', 'salary', 'ppg']
  POSITIONS = ['QB', 'RB', 'WR', 'FLEX', 'D', 'K', 'TE']

  def __init__(self, position_list):
    self._player_list = {}
    self._position_list = position_list
    for pos in position_list:
      self._player_list[pos] = []

  def add_player(self, player):
    """ add a player to the player list """
    self._player_list[player.get_position()].append(player)

  def get_players(self):
    """ get a list of all the players """
    all_players = []
    for position in self._position_list:
      for player in self._player_list[position]:
        all_players.append(player)
    return all_players

  def adjust_for_defenses(self, defense_list):
    ''' adjust for opponent defenses '''
    for position in self._position_list:
      for player in self._player_list[position]:
        adjustment = defense_list.get_adjustment(player.get_opponent())
        if player.get_position() not in ('D', 'K'):
          new_value = player.get_value() * float(adjustment)
          player.set_value(new_value)

  def read_from_draftday_csv(self, csv_path):
    """ read in the players from a draftday csv file """
    file_handler = open(csv_path, 'r')
    file_handler.next()  # skip header row
    csv_reader = csv.DictReader(file_handler, self.DRAFTDAY_FIELDS, ',')
    for line in csv_reader:
      opponent = Teams.Teams().get_by_name(line['opp'])
      player = Player(line['player_name'], line['position'], 
                      line['ppg'], line['salary'], opponent)
      self.add_player(player)

  def get_random_player(self, position=None):
    """ return a random player from the list """
    if position is not None:
      position = re.search(r'[A-Z]*', position).group()  # remove any trailing digits
      random_spot = random.randint(0, len(self._player_list[position]) - 1)
      return self._player_list[position][random_spot]
    else:
      position = self._position_list[random.randint(0, len(self._position_list) - 1)]
      return self._player_list[position][random.randint(0, len(self._player_list))]
