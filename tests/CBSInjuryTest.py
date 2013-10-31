import unittest
from common.injuries import CBSInjuries

class CBSInjuryTest(unittest.TestCase):

  def test_list(self):
    injury_list = CBSInjuries().fetch()
    self.assertGreater(len(injury_list), 10)
