__author__='agni'

import requests

class Crawler:
	#Default implementation. Is overloaded by supplying a queue.
	queue = Util.resolveQueue()

	def __init__(self, queueStr):
		self.queue = Util.resolveQueue(queueStr)

	def fetch():
		return fetch(queue.pop())

	def fetch(url):
		return requests.get(url)

	def write(writer, data):
		writer.write(data)

