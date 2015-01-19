__author__='agni'

import requests
from time import sleep
from urlparse import urlparse

class Crawler:
	#Default implementation. Is overloaded by supplying a queue.
	queue = Util.resolveQueue()
	writer = Util.resolveWriter()

	def __init__(self, queueStr):
		self.queue = Util.resolveQueue(queueStr)

	def fetch(self):
		return self.fetch(self.queue.pop())

	def fetch(self, url):
		config = Util.getSiteConfig(urlparse(url).netloc)
		sleep(config.get("crawl-delay"))
		return requests.get(url)

	def write(self, data):
		self.writer.write(data)

	def fetchAndWrite(self):
		fetched = self.fetch()
		self.write(fetched)
		return fetched

	def fetchAndWrite(self, url):
		fetched = self.fetch(url)
		self.write(fetched)
		return fetched

	# YES! The crawl-till-you-get-blocked. Somebody stop me!!!
	def keepFetching(self):
		self.fetchAndWrite()
		self.keepFetching()

