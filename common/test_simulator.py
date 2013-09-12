import random

varities = range(0,5)
num_per_variety = 100
attempts = 10000

# basic widget
class Widget(object):
  def __init__(self, variety, value, cost):
    self._variety = variety
    self._value = value
    self._cost = cost

  def get_value(self):
    return self._value

  def get_cost(self):
    return self._cost

  def get_variety(self):
    return self._variety

class WidgetList(object):
  def __init__(self, variety_list):
    self._widget_list = {}
    self._varities = variety_list
    for variety in variety_list:
      self._widget_list[variety] = []
 
  def add_widget(self, widget):
    self._widget_list[widget.get_variety()].append(widget)

  def get_widgets(self):
    all_widgets = []
    for variety in self._varities:
      for widget in self._widget_list[variety]:
        all_widgets.append(widget)
    return all_widgets

  def get_random_widget(self, variety=None):
    if variety is not None:
      return self._widget_list[variety][random.randint(0, len(self._widget_list))]
    else:
      variety = random.randint(0, len(self._varities) - 1)
      return self._widget_list[variety][random.randint(0, len(self._widget_list))]
      
class Configuration(object):
  ''' a configuration is a set of widgets, one of each type '''
  
  def __init__(self, max_allowed_cost):
    self._configuration = {}
    self._max_allowed_cost = max_allowed_cost

  def get_cost(self):
    ''' obtain total cost for widgets '''
    return sum([widget.get_cost() for (variety, widget) in self._configuration.items()])

  def get_value(self):
    ''' obtain total value for widgets '''
    return sum([widget.get_value() for (variety, widget) in self._configuration.items()])
 
  def add_widget(self, widget):
    if widget.get_cost() + self.get_cost() > self._max_allowed_cost:
      raise BaseException("cost is too high!")
    else:
      self._configuration[widget.get_variety()] = widget
    

# build our initial test sets
print "building initial sets..."
widgetlist = WidgetList(varities)
for variety in varities:
  for x in range(0, num_per_variety):
    widget = Widget(variety, random.randint(0,100), random.randint(0,100))
    widgetlist.add_widget(widget)

config = Configuration(200)

# put random items in the configuration
for variety in varities:
  w = widgetlist.get_random_widget(variety)
  config.add_widget(w)

print config.get_value()
