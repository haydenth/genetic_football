class Player(object):

  def __init__(self, name, position, value, cost):
    self._position = position
    self._value = value
    self._name = name
    self._cost = cost

  def get_value(self):
    return float(self._value)

  def get_cost(self):
    return int(self._cost)

  def get_position(self):
    return self._position

  def get_name(self):
    return self._name
