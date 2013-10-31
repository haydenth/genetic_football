import time
import urllib2
import gzip
from StringIO import StringIO


class ScraperException(BaseException):
  """ Scraper exception """


class Scraper(object):
  RETRIES = 5
  DEFAULT_BROWSER = 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0)' + \
                    ' Gecko/20100101 Firefox/21.0'
   
  def html(self, url):
    """ return html for a URL, with retries """
    tries = 0
    while tries < self.RETRIES:
      try:
        headers = {'User-Agent': self.DEFAULT_BROWSER}
        req = urllib2.Request(url, None, headers)
        response = urllib2.urlopen(req)

        # see if it's gzipped. if so, ungzip it
        if response.info().get('Content-Encoding') == 'gzip':
          buf = StringIO( response.read())
          f = gzip.GzipFile(fileobj=buf)
          html = f.read() 
        else:
          html = response.read()
        return html
      except:
        print "Error fetching %s, waiting a sec and trying again..." % url
        tries += 1
        time.sleep(2)
        """ do nothing """

    raise ScraperException("Unable to fetch URL: %s" % url)
