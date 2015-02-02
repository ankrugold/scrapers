import re
from urlparse import urlparse

class FileSystemWriter:

	def __init__(self, writerHead):
		self.writerHead = writerHead

	def write(self, url, data):
		parsedUrl = urlparse(url)
		file = open(self.writerHead + parsedUrl.netloc + cleanWithDashes(parsedUrl.path + parsedUrl.query), "w")
		file.write(data)
		file.close()

	def cleanWithDashes(self, str):
		re.sub("[=&/]", "--", str)

