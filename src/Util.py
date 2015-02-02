from pyhocon import ConfigFactory
from InMemoryQueue import InMemoryQueue
from FileSystemWriter import FileSystemWriter

class Util:
	config = ConfigFactory.parse_file("../conf/application.conf")
	queueString = config.get_string("scrapers.queue")
	writerString = config.get_string("scrapers.writer")
	writerHead = config.get_string("scrapers.writer-head")
	def resolveQueue(self, queueStr = queueString):
		queues = { "InMemoryQueue" : InMemoryQueue() }
		return queues[queueStr]
	def resolveWriter(self):
		writers = {	"FileSystemWriter" : FileSystemWriter(self.writerHead)	}
		return writers[self.writerString]
	def getSiteConfig(self, site):
		siteConfig = self.config.get("scrapers.site-config.sites").get(site)