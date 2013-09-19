class Player(object):

  def __init__(self, name, position='', value=0, cost=0, opp=''):
    self._position = position
    self._value = value
    self._name = name
    self._opponent = opp
    self._cost = cost

  def get_value(self):
    return float(self._value)

  def set_value(self, value):
    self._value = value

  def get_cost(self):
    return int(self._cost)

  def get_opponent(self):
    return self._opponent

  def get_position(self):
    return self._position

  def get_name(self):
    return self._name
