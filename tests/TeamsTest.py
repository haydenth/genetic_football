import unittest
from common.team import Teams


class TeamsTest(unittest.TestCase):

  def test_mappings(self):
    ''' test that we have all the mappings there. '''
    self.assertEquals(len(Teams().MAPPING), 32)
    self.assertEquals(Teams().get_by_name('Raiders'), 'OAK')
