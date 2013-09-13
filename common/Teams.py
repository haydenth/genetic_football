class TeamsException(BaseException):
  ''' teams exception holder '''


class Teams(object):
  MAPPING = {'SF': '49ers', 'CHI': 'Bears',
             'CIN': 'Bengals', 'BUF': 'Bills',
             'DEN': 'Broncos', 'CLE': 'Browns',
             'TB': 'Buccaneers', 'ARI': 'Cardinals',
             'SD': 'Chargers', 'KC': 'Chiefs',
             'IND': 'Colts', 'DAL': 'Cowboys',
             'MIA': 'Dolphins', 'PHI': 'Eagles',
             'ATL': 'Falcons', 'NYG': 'Giants',
             'JAC': 'Jaguars', 'DET': 'Lions',
             'GB': 'Packers', 'CAR': 'Panthers',
             'OAK': 'Raiders', 'STL': 'Rams', 'BAL': 'Ravens',
             'WAS': 'Redskins', 'NO': 'Saints',
             'SEA': 'Seahawks', 'PIT': 'Steelers',
             'HOU': 'Texans', 'TEN': 'Titans',
             'NYJ': 'Jets',
             'MIN': 'Vikings', 'NE': 'Patriots'}

  def get_by_name(self, name):
    for (team_id, team) in self.MAPPING.items():
      if name == team:
        return team_id
    raise TeamsException('Team %s not found!' % name)
