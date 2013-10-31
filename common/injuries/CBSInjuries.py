import re
import datetime
import BeautifulSoup
from common.scraper import Scraper


class CBSInjuries(object):
  URL = 'http://www.cbssports.com/nfl/injuries'

  def fetch(self):
    html = Scraper().html(self.URL)
    bs = BeautifulSoup.BeautifulSoup(html)
    data_tables = bs.findAll('table', {'class': 'data'})

    player_results = []
    for data_table in data_tables:
      rows = data_table.findAll('tr', {'class': re.compile('row')})
      for row in rows:
        cols = row.findAll('td')
        if len(cols) < 6:
          continue

        (ds, pos, player,
         injury, nflstatus, news) = [str(col.contents[0]) for col in cols]

        player_name = re.search('\>(.*)\<', player).group(1)
        if re.search('Probable', news):
          severity = 'PROBABLE'
        elif re.search('Questionable', news):
          severity = 'QUESTIONABLE'
        elif re.search('Out', news) or re.search('out', news):
          severity = 'OUT'
        elif re.search('Doubtful', news):
          severity = 'DOUBTFUL'
        elif re.search('Suspended', news):
          severity = 'SUSPENDED'
        else:
          severity = 'OK'

        if len(nflstatus) > 6:
          severity = nflstatus

        ds = datetime.datetime.strptime(ds, '%m/%d/%y').date().isoformat()
        player_results.append({'date': ds, 'position': pos,
                               'name': player_name, 'severity': severity,
                               'injury': injury, 'nflstatus': nflstatus,
                               'news': news})
    return player_results
