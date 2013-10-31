import unittest
from common.team import Teams


class TeamsTest(unittest.TestCase):

  def test_mappings(self):
    self.assertEquals(len(Teams().MAPPING), 32)
    self.assertEquals(Teams().get_by_name('Raiders'), 'OAK')
