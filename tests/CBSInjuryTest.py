import unittest
from common.injuries import CBSInjuries

class CBSInjuryTest(unittest.TestCase):

  def test_list(self):
    ''' Test that we can pull the list and it has at least 10 entries '''
    injury_list = CBSInjuries().fetch()
    self.assertGreater(len(injury_list), 10)
