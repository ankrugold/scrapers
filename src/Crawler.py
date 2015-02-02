__author__='agni'

import requests
from time import sleep
from urlparse import urlparse
from Util import Util

class Crawler:
	#Default implementation. Is overloaded by supplying a queue.
	queue = Util().resolveQueue()
	writer = Util().resolveWriter()

	def __init__(self, queueStr):
		self.queue = Util.resolveQueue(queueStr)
	def fetch(self, url = queue.pop()):
		if url == None: url = self.queue.pop()
		config = Util.getSiteConfig(urlparse(url).netloc)
		sleep(config.get("crawl-delay"))
		return requests.get(url)
	def write(self, data):
		self.writer.write(data)
	def fetchAndWrite(self, url = None):
		fetched = self.fetch(url)
		self.write(fetched)
		return fetched
	# YES! The crawl-till-you-get-blocked. Somebody stop me!!!
	def keepFetching(self):
		self.fetchAndWrite()
		self.keepFetching()

