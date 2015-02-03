__author__='agni'

import requests
import logging
from time import sleep
from urlparse import urlparse
from Util import Util

class Crawler:
	util = Util()
	writer = util.resolveWriter()
	#Default implementation. Is overloaded by supplying a queue.
	def __init__(self, queueStr = "InMemoryQueue"):
		self.queue = self.util.resolveQueue(queueStr)
	def fetch(self, url = None):
		if url == None: url = self.queue.pop()
		self.url = url
		logging.info('Fetching url: ' + url)
		config = self.util.getSiteConfig(urlparse(url).netloc)
		sleep(config.get("crawl_delay"))
		return requests.get(url).text
	def write(self, data):
		self.writer.write(self.url, data)
	def fetchAndWrite(self):
		fetched = self.fetch()
		self.write(fetched)
		return fetched
	def keepFetching(self): # YES! The crawl-till-you-get-blocked. Somebody stop me!!!
		self.fetchAndWrite()
		self.keepFetching()

