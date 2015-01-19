from pyhocon import ConfigFactory

class Util:
	config = ConfigFactory.load()
	queueString = config.getString("scrapers.queue")
	writerString = config.getString("scrapers.writer")
	writerHead = config.getString("scrapers.writer-head")

	def resolveQueue():
		return resolveQueue(queueString)

	def resolveQueue(queueStr):
		queues = { "InMemoryQueue" : InMemoryQueue() }
		return queues[queueStr]

	def resolveWriter():
		writers = {	"FileSystemWriter" : FileSystemWriter()	}
		return writers[writerString]

	def getSiteConfig(site):
		siteConfig = config.get("scrapers.site-config.sites").get(site)