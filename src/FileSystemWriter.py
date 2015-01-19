import re
from urlparse import urlparse

class FileSystemWriter:
	writerHead = Util.writerHead

	def write(url, data):
		parsedUrl = urlparse(url)
		file = open(writerHead + parsedUrl.netloc + cleanWithDashes(parsedUrl.path + parsedUrl.query), "w")
		file.write(data)
		file.close()

	def cleanWithDashes(str):
		re.sub("[=&/]", "--", str)

