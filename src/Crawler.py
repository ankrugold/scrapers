__author__='agni'

from pyhocon import ConfigFactory

class Crawler:
	config = ConfigFactory.load()
	queue = config.getString("scrapers.queue")

	